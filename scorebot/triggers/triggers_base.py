import logging

from scorebot.db import db_api
from scorebot import players
from scorebot.bots.bot_api import BotApi

LOG = logging.getLogger(__name__)


class BaseTrigger:

    def __init__(self, name, get_date_scope, trigger_point,
                 msg=None):
        self.name = name
        self.get_date_scope = get_date_scope
        self.trigger_point = trigger_point
        self.msg = msg

    def _is_trigger_flag_set(self, all_flags, owner):
        """Checks if trigger is set (fired already) for owner

        :param all_flags: all trigger flags in a given date scope.
        :param owner: player name or team name
        :return: bool
        """
        return all_flags.get(owner, False)

    def _set_trigger_flag(self, owner):
        """Sets trigger flag (means trigger fired already) in db

        :param owner: player name or team name
        :return: None
        """
        db_api.TriggerFlag.create(
            set_for_trigger=self.name,
            set_for_owner=owner
        )
        LOG.debug("Set trigger flag '{}' for '{}'".format(self.name, owner))

    def check(self, all_flags, all_scores, owner):
        """Checks trigger condition, and fires if not fired already in a
        given date scope.

        :param all_flags: all trigger flags in a given date scope.
        :param all_scores: all scores in a given date scope
        :param owner: player name or team name
        :return: None
        """
        if self._is_trigger_flag_set(all_flags, owner):
            return

        if all_scores.get(owner, 0) >= self.trigger_point:
            self._set_trigger_flag(owner)
            self.on_fire(owner)

    def on_fire(self, owner):
        """Called when trigger is fired. Used to send notifications, etc.

        :param owner: player name or team name
        :return: None
        """
        pass


class PlayerTrigger(BaseTrigger):
    def on_fire(self, owner):
        """Notifies player team that the player has reached trigger"""
        player_info = players.player_info(owner)
        BotApi.say_to_team(player_info.team, self.msg, player_info)


class TeamTrigger(BaseTrigger):
    def on_fire(self, owner):
        """Notifies all that the team has reached trigger"""
        BotApi.say_to_all(self.msg, owner)


class GroupOfPlayerTriggers:
    def __init__(self, score_db_api, triggers):
        self.score_db_api = score_db_api
        assert all([isinstance(t, PlayerTrigger) for t in triggers])
        self.triggers = triggers

    def check(self):
        for trigger in self.triggers:
            trigger_flags = db_api.TriggerFlag.list_for_trigger(
                trigger.name, trigger.get_date_scope())
            scores = self.score_db_api.counts_per_players(
                trigger.get_date_scope())
            for player in scores.keys():
                trigger.check(trigger_flags, scores, player)


class GroupOfTeamTriggers:
    def __init__(self, score_db_api, triggers):
        self.score_db_api = score_db_api
        assert all([isinstance(t, TeamTrigger) for t in triggers])
        self.triggers = triggers

    def check(self):
        for trigger in self.triggers:
            trigger_flags = db_api.TriggerFlag.list_for_trigger(
                trigger.name, trigger.get_date_scope())
            scores = self.score_db_api.counts_per_teams(
                trigger.get_date_scope())
            for team in scores.keys():
                trigger.check(trigger_flags, scores, team)
