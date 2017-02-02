#!/usr/bin/env bash

db_name="scorebot-db"
target=http://scorebot_backup:5984/$db_name

echo "======== Replicating to read-only DB ============="
replicate_cmd="
curl -X PUT $target &> /dev/null;

curl -X POST -H \"Content-Type: application/json\" \
-d '{\"source\": \"$db_name\", \"target\": \"$target\"}' \
http://localhost:5984/_replicate;
"
echo $replicate_cmd
docker exec -it scorebot_db bash -c "$replicate_cmd"

echo "============ Compressing the data ================"
data_dir="/usr/local/var/lib/couchdb/"
tar_cmd="cd $data_dir && tar -czf db-dump.tar.gz -C $data_dir *.couch"
echo $tar_cmd
docker exec -it scorebot_backup bash -c "$tar_cmd"

echo "============ Copying dump to host  ==============="
mkdir -p backups
backup_name=./backups/scorebot-db-$(date +%Y-%m-%d.%H:%M:%S).tar.gz
docker cp scorebot_backup:$data_dir/db-dump.tar.gz $backup_name

echo
echo "Done, find $backup_name"
