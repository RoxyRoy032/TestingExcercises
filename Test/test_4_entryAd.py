import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.ActionPage import ActionPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains


class TestExcercise4(BaseClass):

    def test_4_disappearingElements(self):
        # Home page menu - Entry Ad
        homePage = HomePage(self.driver)
        homePage.entryAd().click()

        #Model page
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='modal']/div[2]/div[3]/p"))).click()
        time.sleep(2)
        # wait until 2 seconds

        #Refresh page
        self.driver.refresh()
        time.sleep(2)
        # wait until 2 seconds

        #It takes a double click
        actions = ActionChains(self.driver)
        actions.double_click(self.driver.find_element_by_link_text("click here")).perform()
        time.sleep(2)
        # wait until 2 seconds