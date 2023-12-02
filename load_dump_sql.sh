#!/bin/bash

DATABASE_CONTAINER_ID=$1
PRESTASHOP_CONTAINER_ID=$2
PASS=$3
docker cp ./mysql/dump.sql $DATABASE_CONTAINER_ID:/tmp/dump.sql
docker exec $DATABASE_CONTAINER_ID bash -c "mysql -u root --password=${PASS}  < /tmp/dump.sql"
docker exec $DATABASE_CONTAINER_ID bash -c "rm -rf /tmp/dump.sql"
