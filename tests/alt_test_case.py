import unittest
import time
import os
from appium import webdriver

from alttester import AltDriver


class AltTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = os.getenv('APPIUM_PLATFORM', 'IOS')
        cls.desired_caps['deviceName'] = os.getenv(
            'APPIUM_DEVICE', 'Local Device')
        cls.desired_caps['app'] = os.getenv(
            "APPIUM_APPFILE", "$PWD/app/TrashCat.ipa")
        cls.desired_caps['automationName'] = os.getenv(
            'APPIUM_AUTOMATION', 'XCUITest')
        cls.desired_caps['xcodeorgid'] = os.getenv(
            'APPIUM_XCODEORGID', '59ESG8ELF5')
        cls.desired_caps['xcodesignid'] = os.getenv(
            'APPIUM_XCODESIGNID', 'iPhone Developer')

        cls.appium_driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', cls.desired_caps)
        print("Appium driver started")
        time.sleep(10)
        cls.altdriver = AltDriver(enable_logging=False)

    @classmethod
    def tearDownClass(cls):
        print('Ending')
        cls.altdriver.stop()
        cls.appium_driver.quit()
