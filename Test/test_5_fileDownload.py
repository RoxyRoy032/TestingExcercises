import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.ActionPage import ActionPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains


class TestExcercise5(BaseClass):

    def test_5_fileDownload(self):
        # Home page menu - File Download
        homePage = HomePage(self.driver)
        homePage.fileDownload().click()

        #Click on download link
        self.driver.find_element_by_link_text("some-file.txt").click()
        time.sleep(2)
        # wait until 2 seconds