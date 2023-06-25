#!/usr/bin/env bash
# exit on error
set -o errexit

make install
python manage.py collectstatic --no-input
make migrate
