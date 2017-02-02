import logging

from scorebot.triggers.player_triggers import player_triggers
from scorebot.triggers.team_triggers import team_triggers


LOG = logging.getLogger(__name__)


def check_triggers_for_score(score_type):
    LOG.debug("Checking player triggers")
    player_triggers[score_type].check()
    LOG.debug("Checking team triggers")
    team_triggers[score_type].check()
