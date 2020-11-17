from selenium.webdriver.common.by import By

from TestData.TestData import TestData


class HomePage():



    def __init__(self, driver):
        self.driver = driver
        testData = TestData()
        self.test_HomePage_data = testData.getHomePageData()

    def addRemoveElement(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[0])

    def contextMenu(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[1])

    def disappearingElements(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[2])

    def entryAd(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[3])

    def fileDownload(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[4])

    def fileUpload(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[5])

    def formAuthentication(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[6])

    def javaScriptAlerts(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[7])

    def keyPresses(self):
        return self.driver.find_element(By.LINK_TEXT, self.test_HomePage_data[8])