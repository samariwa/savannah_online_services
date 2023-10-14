#!/bin/bash
# A script that builds the app
echo "starting build..."
echo "setting up virtual environment..."
source env/bin/activate
echo "checking for app dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=run.py
export FLASK_DEBUG=1
echo "configuring server..."
./server_config.sh