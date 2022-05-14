#!/usr/bin/env bash
# exit on error
set -o errexit

gunicorn Portfolio2022.wsgi:application