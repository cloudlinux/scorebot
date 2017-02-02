import logging
import os

import pycouchdb

from scorebot.db import db_utils

LOG = logging.getLogger(__name__)

DB_NAME = 'scorebot-db'

db_addr = os.environ.get("DB_ADDR", "127.0.0.1")
server = pycouchdb.Server("http://{}:5984/".format(db_addr))
if DB_NAME in server:
    DB = server.database(DB_NAME)
else:
    DB = server.create(DB_NAME)


class BaseScore:
    type = "base_score"
    required_fields = ("player_name", "player_team")

    @classmethod
    def create(cls, data):
        """Saves score to db"""
        doc = {
            "type": cls.type,
            **data
        }
        db_utils.set_created_at(doc)
        LOG.debug("Adding score {} with data: {}".format(cls.type, data))
        return DB.save(doc)

    @classmethod
    def counts_per_players(cls, date_scope):
        """Gets score counts per player in a date scope

        :param date_scope: in what date scope
        :return: Dict {player: score_count}
        """
        return cls._counts_per("player_name", date_scope)

    @classmethod
    def counts_per_teams(cls, date_scope):
        """Gets score counts per team in a date scope

        :param date_scope: in what date scope
        :return: Dict {team: score_count}
        """
        return cls._counts_per("player_team", date_scope)

    @classmethod
    def _counts_per(cls, per, date_scope):
        map = """
        function(doc) {
            if (%s && doc.type == '%s') {
                emit(doc.%s, 1);
            }
        }""" % (date_scope, cls.type, per)
        reduce = "_sum"

        res = {}
        for record in DB.temporary_query(map, reduce, group='true'):
            owner = record['key']
            score_count = record['value']
            res[owner] = score_count
        return res
