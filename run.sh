#!/bin/sh
cd /home/pi/dev/check-co2
. ./venv/bin/activate
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/dev/check-co2/google_application_credentials.json"
python main.py
deactivate
