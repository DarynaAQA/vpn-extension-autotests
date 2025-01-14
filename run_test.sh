#!/usr/bin/env bash

pip install --upgrade pip
pip install -r requirements.txt

pytest --browser='chrome' tests
#pytest --browser='firefox' tests




