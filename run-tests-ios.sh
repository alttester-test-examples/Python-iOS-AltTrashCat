#!/bin/bash

echo "==> Print decives."
instruments -s devices

# echo "==> Installing a clean build of Endless Runner:"
# xcodebuild clean build-for-testing -scheme Unity-iPhone -destination generic/platform=iOS
# xcodebuild test-without-building -destination "platform=iOS,id=$DEVICE_UDID" -scheme Unity-iPhone &

# echo "==> Installing dependencies"
# chmod 0755 requirements.txt
# python3 -m pip install -r requirements.txt

# echo "==> Port forwarding to 13000:"
# iproxy 13000 13000 $DEVICE_UDID &
# sleep 60

# cd "../../alttrashcatj"
# dotnet restore

# echo "==> Run tests"
# rm -rf screenshots
# python3 -m pytest tests/ -s

# echo "==> Killing existing xcode processes:"
# killall xcodebuild || true
# killall iproxy
