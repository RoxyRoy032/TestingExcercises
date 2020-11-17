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


class TestExcercise7(BaseClass):

    def test_7_fileUpload(self):
        # Home page menu - Form Authentication
        homePage = HomePage(self.driver)
        homePage.formAuthentication().click()

        #Login Success
        time.sleep(2)
        # wait until 2 seconds
        actionPage = ActionPage(self.driver)
        testData = TestData()
        actionPage.loginTest(testData.getUsersData()[0][0], testData.getUsersData()[0][1])
        time.sleep(2)
        # wait until 2 seconds
        self.driver.find_element_by_xpath("//*[@id='login']/button").click()
        time.sleep(2)
        # wait until 2 seconds

        #Logout button
        time.sleep(2)
        # wait until 2 seconds
        self.driver.find_element_by_xpath("//*[@id='content']/div/a").click()
        time.sleep(2)
        # wait until 2 seconds

        #Login failed
        time.sleep(2)
        # wait until 2 seconds
        actionPage.loginTest(testData.getUsersData()[1][0], testData.getUsersData()[1][1])
        #“Your password is invalid!” Message
        time.sleep(2)
        # wait until 2 seconds
        self.driver.find_element_by_xpath("//*[@id='login']/button").click()
        time.sleep(2)
        # wait until 2 seconds
