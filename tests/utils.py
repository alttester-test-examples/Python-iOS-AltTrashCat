import unittest
import sys
import time
import os
from appium import webdriver

from alttester.portforwarding import AltPortForwarding
from alttester import AltDriver

sys.path.append(os.path.dirname(__file__))


class AltTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = os.getenv('APPIUM_PLATFORM', 'IOS')
        cls.desired_caps['deviceName'] = os.getenv('APPIUM_DEVICE', 'Local Device')
        cls.desired_caps['app'] = os.getenv("APPIUM_APPFILE", "$PWD/app/TrashCat.ipa")
        cls.desired_caps['automationName'] = os.getenv('APPIUM_AUTOMATION', 'XCUITest')
        cls.desired_caps['xcodeorgid'] = os.getenv('APPIUM_XCODEORGID', '59ESG8ELF5')
        cls.desired_caps['xcodesignid'] = os.getenv('APPIUM_XCODESIGNID', 'iPhone Developer')

        cls.appium_driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        print("Appium driver started")
        cls.setup_port_forwarding()
        time.sleep(10)
        cls.altdriver = AltDriver(enable_logging=False)

    @classmethod
    def setup_port_forwarding(cls):
        try:
            AltPortForwarding.kill_all_iproxy_process()
        except:
            print("No iproxy forward was present")
        AltPortForwarding.forward_ios()
        print("Port forwarded (iOS).")

    @classmethod
    def tearDownClass(cls):
        print('Ending')
        cls.altdriver.stop()
        cls.appium_driver.quit()