import logging
import sys

from aiohttp import web

from scorebot import players

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
LOG = logging.getLogger(__name__)


def get_player_team(data):
    if "player_name" not in data:
        msg = "Missing 'player_name' in body"
        LOG.debug(msg)
        raise web.HTTPBadRequest(text=msg)

    player = data['player_name']
    try:
        team = players.player_info(player).team
    except players.PlayerNotFound:
        msg = "Unregistered player '{}'".format(player)
        LOG.debug(msg)
        raise web.HTTPBadRequest(text=msg)

    return team


def validate_score(data, add_req_keys=set(), add_restr_keys=set()):
    given_keys = set(data.keys())

    req_keys = {'player_name'}
    req_keys.update(add_req_keys)

    restr_keys = {'created_at'}
    restr_keys.update(add_restr_keys)

    missing_keys = req_keys - given_keys
    if missing_keys:
        msg = ("Given body '{}' is missing the following "
               "keys '{}'".format(given_keys, missing_keys))
        LOG.debug(msg)
        raise web.HTTPBadRequest(text=msg)

    restricted_keys = restr_keys.intersection(given_keys)
    if restricted_keys:
        msg = ("Given body '{}' contain the following restricted "
               "keys '{}'".format(given_keys, restricted_keys))
        LOG.debug(msg)
        raise web.HTTPBadRequest(text=msg)
