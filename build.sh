#!/usr/bin/env bash
# exit on error
set -o errexit

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python3 manage.py collectstatic --no-input
python3 manage.py migrate