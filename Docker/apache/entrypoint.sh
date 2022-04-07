#!/usr/bin/env bash

set -e

until pg_isready -h 'postgres' -U 'iriusprod' -t 3 -q; do
  >&2 echo "Postgres is unavailable - trying again in 3 seconds"
  sleep 3
done

>&2 echo "Postgres is ready"

apache2ctl -D FOREGROUND