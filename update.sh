#!/usr/bin/env bash

dtstamp=$(date +%Y%m%d_%H%M%S)
. ~/.virtualenvs/business_licenses/bin/activate

git pull
./licenses.py
git add -A
git commit -m "$dtstamp"
git push

deactivate