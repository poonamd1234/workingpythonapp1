#!/bin/bash

set -x

pip3 install virtualenv

cd /aiBot

python3 -m venv env

mkdir db

source /aiBot/env/bin/activate

pip install --no-cache-dir -r ./requirements.txt

python3 manage.py migrate
