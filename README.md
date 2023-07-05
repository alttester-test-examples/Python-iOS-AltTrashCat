# Python - iOS - AltTrashCat

This repository shows a few Python tests that use the page object model and AltTester Unity SDK to test the Unity endless runner sample:
https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

### Before running the tests on iOS
- in the `run-tests-ios.sh` script please change the value for `APPIUM_XCODEORGID` with your Team ID (uniquie 10-character string) in Apple dev account
- export `IOS_UDID=<your-device-udid>` then run the script `run-tests-ios.sh`
- considering that `port forwarding` is no longer available on iOS devices, to be able to use port forwarding it is necessary to follow the steps from https://alttester.com/docs/desktop/v.2.0.1/pages/known-issues.html#problem-with-reverse-port-forwarding-for-ios
## Running tests

> **Note**: The tests are meant to be run on an iOS device.

1. Install the [AltTesterDesktop](https://alttester.com/alttester/#pricing), then open it (you need to accept the Terms and Conditions if the AltTester is opened for the first time).
2.  Create a folder `app` under project. The app is provided at https://alttester.com/app/uploads/AltTester/TrashCat/TrashCatiOS2_0_1.ipa.zip and needs to be included unzipped under app/ folder.
3. To start the tests run:

    ```
    $ ./run-tests-ios.sh
    ```

This script will:

- start the app on your device
- run the tests
- stop the app after the test are done
