import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.ActionPage import ActionPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains


class TestExcercise3(BaseClass):

    def test_3_disappearingElements(self):
        # Home page menu - Disapperaring Elements
        homePage = HomePage(self.driver)
        homePage.disappearingElements().click()

        #Visible object
        while True:
            elem = self.driver.find_elements_by_xpath("//*[@id='content']/div/ul/li[5]/a")
            if len(elem) > 0:
                break
            else:
                self.driver.refresh()
        time.sleep(2)
        # wait until 2 seconds

        #Not visible object
        while True:
            elem = self.driver.find_elements_by_xpath("//*[@id='content']/div/ul/li[5]/a")
            if len(elem) > 0:
                self.driver.refresh()
            else:
                break
        time.sleep(2)
        # wait until 2 seconds

