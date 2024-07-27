from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
from .WebDriver import *

class MySeleniumTests(LiveServerTestCase):
    #fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(browser.chrome).driver

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        driver = self.selenium
        driver.get('http://127.0.0.1:8000/')
        driver.implicitly_wait(300)
        #self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        #username_input = self.selenium.find_element(By.NAME, "username")
        #username_input.send_keys('myuser')
        #password_input = self.selenium.find_element(By.NAME, "password")
        #password_input.send_keys('secret')
        #self.selenium.find_element(By.CLASS_NAME, 'btn').click()
        #self.selenium.find_element(By.CLASS_NAME, 'navbar-brand')