from enum import Enum
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.edge.service import Service as edgeService
from selenium import webdriver


class browser(Enum):
    firefox = 'firefox'
    chrome = 'chrome'
    edge = 'edge'

class WebDriver:

    def __init__(self, browser):
        self.browser = browser
        self.driver = getWebDriver(browser)



## SETUP


def getWebDriver(browser= browser.chrome):
    service = None
    options = None
    port = 12345
    if browser == browser.chrome:
        service = webdriver.ChromeService(executable_path=getDriverPath(browser), port=port, service_args=list('--verbose'))
        options = webdriver.ChromeOptions()
    elif browser == browser.firefox:
        service = webdriver.FirefoxService(executable_path=getDriverPath(browser), port=port, service_args=list('--verbose'))
        options = webdriver.FirefoxOptions()
    else:
        service = webdriver.EdgeService(executable_path=getDriverPath(browser), port=port, service_args=list('--verbose'))
        options = webdriver.EdgeOptions()
    return setUpDriver(browser, service, options)


def setUpDriver(browser, service, options):
    driver = None
    if browser == browser.chrome:
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == browser.firefox:
        driver = webdriver.Firefox(service=service, options=options)
    else:
        driver = webdriver.Edge(service=service, options=options)
    return driver

def getDriverPath(browser=browser.chrome):
    base_path = "C:/WebDriver/"
    driver_path = ''
    if browser == browser.chrome:
        driver_path = "chromedriver-win32/chromedriver.exe"
    elif browser == browser.firefox:
        driver_path = "geckodriver-v0.34.0-win32/geckodriver.exe"
    else:
        driver_path = "edgedriver_win64/msedgedriver.exe"
    return base_path + driver_path


## TEARDOWN

def tearDownDriver(driver):
    driver.quit()
    return None