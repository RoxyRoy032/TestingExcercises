import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from TestData.TestData import TestData
from pageObjects.ActionPage import ActionPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains


class TestExcercise6(BaseClass):

    def test_6_fileUpload(self):
        # Home page menu - File Upload
        homePage = HomePage(self.driver)
        homePage.fileUpload().click()

        #Upload file
        time.sleep(2)
        # wait until 2 seconds
        testData = TestData()
        self.driver.find_element_by_id("file-upload").send_keys(testData.getPathFileData()[0])
        time.sleep(2)
        # wait until 2 seconds

        #Click on submit button
        self.driver.find_element_by_id("file-submit").click()
        time.sleep(2)
        # wait until 2 seconds

