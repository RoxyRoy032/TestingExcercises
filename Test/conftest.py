import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    #Browser name in cmd
    browser_name = request.config.getoption("browser_name")
    #Location of webdriver for browsers
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=r'D:\Selenium\chromedriver.exe')
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=r'D:\Selenium\geckodriver.exe')
    elif browser_name == "IE":
        driver = webdriver.Ie(executable_path=r'D:\Selenium\IEDriverServer.exe')
    #Testing page
    driver.implicitly_wait(3)
    driver.get("https://ss-testing-automated-exercise.herokuapp.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    return driver