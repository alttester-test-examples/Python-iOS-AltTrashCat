import os
import sys

sys.path.append(os.path.dirname(__file__))

from alttester import AltDriver
import unittest
import pytest

class TestBase(unittest.TestCase):
    plaform = os.getenv('TESTS_PLATFORM', 'android')

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltDriver()

    @classmethod    
    def tearDownClass(cls):
        cls.altdriver.stop()
