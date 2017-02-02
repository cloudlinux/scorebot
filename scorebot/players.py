from collections import namedtuple
from config.config import CONF

PlayerInfo = namedtuple('PlayerInfo', ['team', 'slack_name'])


class PlayerNotFound(Exception):
    def __init__(self, player):
        msg = "Player '{}' cannot be found in player-to-team " \
              "mapping.".format(player)
        super(PlayerNotFound, self).__init__(msg)


def player_info(player):
    try:
        return PlayerInfo(*CONF['players'][player])
    except KeyError:
        raise PlayerNotFound(player)
