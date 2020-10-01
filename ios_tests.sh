#!/bin/bash

echo "Installing dependencies"
chmod 0755 requirements.txt
python3 -m pip install -r requirements.txt


## check iproxy
iproxy --version

## Run the test:
echo "Running tests"

rm -rf screenshots
python3 -m pytest tests/ -s

echo "Tests done"