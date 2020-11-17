import time

import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions, wait

from TestData.TestData import TestData
from pageObjects.ActionPage import ActionPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains


class TestExcercise8(BaseClass):

    def test_8_fileUpload(self):
        # Home page menu - JavaScript Alerts
        homePage = HomePage(self.driver)
        homePage.javaScriptAlerts().click()

        #Press button to display alert
        self.driver.find_element_by_xpath("//*[@id='content']/div/ul/li[1]/button").click()
        time.sleep(2)
        # wait until 2 seconds

        #Displayed alert
        alert = self.driver.switch_to.alert
        time.sleep(2)
        # wait until 2 seconds

        #JavaScript alert
        alert.accept()
        self.driver.find_element_by_xpath("//*[@id='content']/div/ul/li[3]/button").click()
        time.sleep(2)

        #Type "testing"
        testData = TestData()
        alert.send_keys(testData.getTextData()[0])
        time.sleep(2)
        # wait until 2 seconds

        #Typed "testing"
        alert.accept()
        time.sleep(2)
        # wait until 2 seconds
