import logging

from config.config import CONF
from scorebot.bots.slack_bot import SlackBot

LOG = logging.getLogger(__name__)


class BotApi:
    bots = [SlackBot]

    @classmethod
    def say_to_all(cls, message, owner):
        """
        Post message to cross-team channel

        :param message: non-formatted message
        :param owner: str(team_name) or player_info, whom this message is about
        :return: None
        """
        thread = CONF['slack_channels']['cross-team']
        cls._bots_say(thread, message, owner)

    @classmethod
    def say_to_team(cls, team, message, owner):
        """
        Post message to team channel

        :param team: which team to post to
        :param message: non-formatted message
        :param owner: str(team_name) or player_info, whom this message is about
        :return: None
        """
        thread = CONF['slack_channels'][team]
        cls._bots_say(thread, message, owner)

    @classmethod
    def _bots_say(cls, dest, message, owner):
        for bot in cls.bots:
            try:
                bot.say(dest, message, owner)
            except Exception as e:
                LOG.error("Exception during '{}' say: {}".format(
                    repr(bot), repr(e)))
