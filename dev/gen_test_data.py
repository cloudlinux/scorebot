# run:
# python dev/gen_test_data.py

# run in docker:
# docker exec -it scorebot_api python dev/gen_test_data.py

import os
from random import choice
import pycouchdb


db_addr = os.environ.get("DB_ADDR", "127.0.0.1")
DB_NAME = 'scorebot-db'
server = pycouchdb.Server("http://{}:5984/".format(db_addr))
if DB_NAME in server:
    _db = server.database(DB_NAME)
else:
    _db = server.create(DB_NAME)

# creates 15k documents (rough - monthly scores)
for bulk in range(15):
    docs = [{"player_name": choice(("mlobur", "rsabitov")),
             "player_team": "st3",
             "type": choice(("patchset_proposed",
                             "patchset_merged",
                             "patchset_reviewed",
                             )),
             "created_at": {
                 "year": 2016,
                 "day_of_year": 207,
                 "month": 7,
                 "week_of_year": 30
             }} for _ in range(1000)]
    _db.save_bulk(docs)
