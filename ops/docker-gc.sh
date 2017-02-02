#!/usr/bin/env bash

docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v /etc:/etc spotify/docker-gc
docker volume rm $(docker volume ls -qf dangling=true)
