import time
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestExcercise1(BaseClass):

    def test_1_addRemoveElements(self):
        #Home page menu - Add/Remove Elements option
        homePage = HomePage(self.driver)
        homePage.addRemoveElement().click()

        #Add 20 elements
        for n in range(0,20):
            self.driver.find_element_by_xpath("//*[@id='content']/div/button").click()
        time.sleep(2)
        #wait until 2 seconds

        #Remove 20 elements
        for n in range(0,20):
            self.driver.find_element_by_class_name("added-manually").click()
        time.sleep(2)
        # wait until 2 seconds