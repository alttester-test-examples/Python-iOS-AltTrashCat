# Python - iOS - AltTrashCat

This repository shows a few Python tests that use the page object model and AltTester Unity SDK to test the Unity endless runner sample:
https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

### Before running the tests on iOS
- in the `run-tests-ios.sh` script please change the value for `APPIUM_XCODEORGID` with your Team ID (uniquie 10-character string) in Apple dev account
- export `IOS_UDID=<your-device-udid>` then run the script `run-tests-ios.sh`

## Running tests

> **Note**: The tests are meant to be run on an iOS device.

Create a folder `app` under project.
The app is provided at https://altom.com/app/uploads/AltTester/TrashCat/TrashCat.ipa.zip and needs to be included unzipped under app/ folder.
To start the tests run:

```
$ ./run-tests-ios.sh
```

This script will:

- start the app on your device
- run the tests
- stop the app after the test are done
