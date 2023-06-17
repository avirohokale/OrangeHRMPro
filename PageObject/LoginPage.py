import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:

    text_username = (By.NAME, "username")
    text_password = (By.NAME, "password")
    text_login = (By.XPATH, "//button[normalize-space()='Login']")
    click_menu_Xpath = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    test_logout = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        time.sleep(2)
        self.wait = WebDriverWait(driver, 5)

    def enter_username(self, username):
        self.wait.until(expected_conditions.presence_of_element_located(self.text_username))
        self.driver.find_element(*Login.text_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Login.text_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Login.text_login).click()

    def login_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.click_menu_Xpath))
            self.driver.find_element(*Login.click_menu_Xpath).click()
            return True
        except NoSuchElementException:
            return False

    def click_menu(self):
        self.driver.find_element(*Login.click_menu_Xpath).click()

    def click_logout(self):
        self.driver.find_element(*Login.test_logout).click()
