# Python - iOS - AltTrashCat

This repository shows a few Python tests that use the page object model and AltTester® Unity SDK to test the Unity Endless Runner sample:
https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

### Before running the tests on iOS
- in the `run-tests-ios.sh` script please change the value for `APPIUM_XCODEORGID` with your Team ID (unique 10-character string) in the Apple dev account
- export `IOS_UDID=<your-device-udid>` then run the script `run-tests-ios.sh`
- considering that the IProxy does not have a way of setting up `reverse port forwarding`, to be able to connect it is necessary to follow the steps from https://alttester.com/docs/sdk/latest/pages/advanced-usage.html#in-case-of-ios 

## Running tests

> **Note**: The tests are meant to be run on an iOS device.

❗ Starting with version 2.0.0, the AltTester® Desktop must be running on your PC while the tests are running.
1. Download and install the AltTester® Desktop for MacOS from [here](https://alttester.com/downloads/), then open it.
2. Instrument the TrashCat application using the latest version of AltTester® Unity SDK - for additional information you can follow [this tutorial](https://alttester.com/walkthrough-tutorial-upgrading-trashcat-to-2-0-x/#Instrument%20TrashCat%20with%20AltTester%20Unity%20SDK%20v.2.0.x)
3. Create a folder `app` under the project and include the instrumented app under it.
4. To start the tests run:

    ```
    $ ./run-tests-ios.sh
    ```

This script will:

- start the app on your device
- run the tests
- stop the app after the tests are done
