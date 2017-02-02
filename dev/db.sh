#!/usr/bin/env bash

docker run -d -p 5984:5984 --name couchdb-dev lobur/couchdb:1.6.1
