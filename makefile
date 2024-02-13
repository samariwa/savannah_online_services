#!/bin/bash
# A makefile that builds the app

all: start_build install_dependencies set_flask_run_file enable_debugging configure_server

start_build:
	@echo "starting build..."

install_dependencies:
	@echo "checking for app dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt

set_flask_run_file:
	export FLASK_APP=run.py

enable_debugging:
	export FLASK_DEBUG=1

configure_server:
	echo "configuring server..."
	./server_config.sh