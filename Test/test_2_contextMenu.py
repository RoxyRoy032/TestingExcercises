import time

import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains


class TestExcercise2(BaseClass):

    def test_2_contextMenu(self):
        # Home page menu - Context Menu
        homePage = HomePage(self.driver)
        homePage.contextMenu().click()

        #Select context menu
        actions = ActionChains(self.driver)
        actions.context_click(self.driver.find_element_by_id("hot-spot")).perform()
        time.sleep(2)
        # wait until 2 seconds

        #Model page - Accept option
        self.driver.switch_to.alert.accept()
        time.sleep(2)
        # wait until 2 seconds



