from selenium.webdriver.common.by import By


class ActionPage:
    def __init__(self, driver):
        self.driver = driver

    def loginTest(self, username, password):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)

