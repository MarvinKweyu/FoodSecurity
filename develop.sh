#!/bin/sh

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
mercury add health-condition.ipynb
mercury add market-gap.ipynb
mercury add pasture-country-averages.ipynb
export WELCOME=welcome.md
mercury runserver --runworker
