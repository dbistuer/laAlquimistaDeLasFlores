from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from ..models import User,Identification


class MySeleniumTests(StaticLiveServerTestCase):
    #fixtures = ["user-data.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    def setUp(self):
        User.objects.create_user(username='dani',
                                first_name='Daniel',
                                last_name='Bistuer',
                                identification=Identification.objects.create(NIF_NIE='78094395B',
                                                                             is_National=True),
                                phone='666666666',
                                email='dbistuer@msn.com',
                                password='Test1234.',
                                is_client=True)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_signup(self):
        driver = self.selenium
        go_home_page(self)
        click(driver, By.NAME, 'dropUser')
        click(driver, By.LINK_TEXT, "Sign in")
        send_keys(driver, By.NAME, 'username', 'daniel')
        send_keys(driver, By.NAME, 'first_name', 'Daniel')
        send_keys(driver, By.NAME, 'last_name', 'Bistuer')
        send_keys(driver, By.NAME, 'identification', '78094396B')
        send_keys(driver, By.NAME, 'phone', '666666666')
        send_keys(driver, By.NAME, 'email', 'danielbistuer@gmail.com')
        send_keys(driver, By.NAME, 'password', 'Test1234.')
        send_keys(driver, By.ID, 'confirmPassword', 'Test1234.')
        driver.implicitly_wait(float(100))
        click(driver, By.ID, 'submit')
        self.assertIn('Iniciar sesión', driver.title)

    def test_login(self):
        driver = self.selenium
        driver.get(f"{self.live_server_url}")
        click(driver, By.NAME, 'dropUser')
        click(driver, By.LINK_TEXT, "Iniciar sesión")
        send_keys(driver, By.NAME, 'username', 'dani')
        send_keys(driver, By.NAME, 'password', 'Test1234.')
        click(driver, By.CLASS_NAME, 'btn-primary')
        self.assertIn('Inicio', driver.title)
        self.assertIn('dani', driver.page_source)

    def test_logout(self):
        self.test_login()
        driver = self.selenium
        click(driver, By.NAME, 'dropUser')
        click(driver, By.LINK_TEXT, "Cerrar sesión")
        self.assertIn('Sesión terminada', driver.title)

    def test_password_change(self):
        self.test_login()
        driver = self.selenium
        click(driver, By.NAME, 'dropUser')
        click(driver, By.LINK_TEXT, "Cambiar contraseña")
        send_keys(driver, By.NAME, 'old_password', 'Test1234.')
        send_keys(driver, By.NAME, 'new_password1', 'Test1234.')
        send_keys(driver, By.NAME, 'new_password2', 'Test1234.')
        click(driver, By.CLASS_NAME, 'btn-primary')
        self.assertIn('Password changed', driver.title)


def go_home_page(self):
    self.selenium.get(f"{self.live_server_url}")

def click(driver,selector,value):
    driver.find_element(selector, value).click()

def send_keys(driver,selector,value,keys):
    driver.find_element(selector, value).send_keys(keys)
