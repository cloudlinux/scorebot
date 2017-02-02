#!/usr/bin/env bash

if [ -z "$1" ]; then echo "Specify backup file to restore"; exit 1; fi

echo "============== Copying dump to DB ================"
docker cp ./$1 scorebot_db:/usr/local/var/lib/db-dump.tar.gz

echo "============ Uncompressing the data =============="
tar_cmd="cd /usr/local/var/lib && rm -rf couchdb/* && tar -zxvf db-dump.tar.gz -C couchdb/"
echo $tar_cmd
docker exec -it scorebot_db bash -c "$tar_cmd"

echo "========== Restarting DB to load data ============"
restart_cmd="curl -X POST -H 'Content-Type: application/json' http://localhost:5984/_restart"
echo $restart_cmd
docker exec -it scorebot_db bash -c "$restart_cmd"
echo "Waiting for DB to start.."
sleep 3

echo "============== Restored DB stats ================="
stats_cmd="curl http://localhost:5984/scorebot-db"
docker exec -it scorebot_db bash -c "$stats_cmd"

echo
echo "Done."