#!/bin/sh
POSTGRES="gosu postgres"

$POSTGRES postgres --single -E <<EOSQL
CREATE ROLE fixmystreet ENCRYPTED PASSWORD 'fixmystreet' LOGIN;
EOSQL
$POSTGRES postgres --single -E <<EOSQL
CREATE DATABASE fixmystreet OWNER fixmystreet ;
EOSQL
$POSTGRES pg_ctl -w start
$POSTGRES psql -d fixmystreet -c 'CREATE EXTENSION postgis;'
$POSTGRES psql -d fixmystreet -c 'GRANT ALL ON geometry_columns TO PUBLIC;'
$POSTGRES psql -d fixmystreet -c 'GRANT ALL ON spatial_ref_sys TO PUBLIC;'
if [ -d /docker-entrypoint-initdb.d ]; then
    for f in /docker-entrypoint-initdb.d/*.dump; do
        [ -f "$f" ] && $POSTGRES psql -d fixmystreet -f "$f"
    done
fi
$POSTGRES pg_ctl stop