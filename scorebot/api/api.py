import logging
import sys

from aiohttp import web

from scorebot.api import api_utils
from scorebot.db import db_api
from scorebot.triggers.check import check_triggers_for_score

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
LOG = logging.getLogger(__name__)


async def _handle_score_request(score_db_api, request):
    data = await request.json()
    LOG.debug("handle_score_request '{}'; Body '{}'".format(request, data))

    data['player_team'] = api_utils.get_player_team(data)
    api_utils.validate_score(data, score_db_api.required_fields)
    score_db_api.create(data)

    check_triggers_for_score(score_db_api.type)
    return web.Response()


async def patchset_proposed(request):
    return await _handle_score_request(db_api.PatchsetProposed, request)


async def patchset_merged(request):
    return await _handle_score_request(db_api.PatchsetMerged, request)


async def patchset_reviewed(request):
    return await _handle_score_request(db_api.PatchsetReviewed, request)


def get_app(loop=None):
    app = web.Application(loop=loop, debug=True)
    app.router.add_route("POST", "/scores/patchset_proposed", patchset_proposed)
    app.router.add_route("POST", "/scores/patchset_merged", patchset_merged)
    app.router.add_route("POST", "/scores/patchset_reviewed", patchset_reviewed)
    return app
