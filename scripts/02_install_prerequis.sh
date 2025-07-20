#!/bin/bash
set -e
source .venv/bin/activate
pip install --upgrade pip
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
pip install -r model/requirements.txt
