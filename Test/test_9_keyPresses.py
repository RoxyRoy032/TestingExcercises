import time
import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions, wait
from pageObjects.ActionPage import ActionPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestExcercise9(BaseClass):

    def test_9_keyPresses(self):
        # Home page menu - Key Presses
        homePage = HomePage(self.driver)
        homePage.keyPresses().click()

        # Press "ESC" key
        self.driver.find_element_by_id("target").send_keys(Keys.ESCAPE)
        time.sleep(2)
        # wait until 2 seconds
        self.driver.find_element_by_id("target").clear()
        time.sleep(2)
        # wait until 2 seconds

        # Press "Space" key
        self.driver.find_element_by_id("target").send_keys(Keys.SPACE)
        time.sleep(2)
        # wait until 2 seconds
        self.driver.find_element_by_id("target").clear()
        time.sleep(2)
        # wait until 2 seconds

        #Press "Back_Space" key
        self.driver.find_element_by_id("target").send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        # wait until 2 seconds
        self.driver.find_element_by_id("target").clear()
        time.sleep(2)
        # wait until 2 seconds