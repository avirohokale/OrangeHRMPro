import time

from PageObject.LoginPage import Login
from utilities.ReadConfigFile import Readvalue

class Test_url_login:
    username = Readvalue.get_username()
    password = Readvalue.get_password()

    def test_url001(self, setup):
        time.sleep(2)
        self.driver = setup

        if self.driver.title == "OrangeHRM":
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\OrangeHRMPro\\ScreenShot\\test_001_Pass.png")

            assert True

        else:
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\OrangeHRMPro\\ScreenShot\\test_001_Fail.png")

            assert False
        self.driver.close()

    def test_login002(self, setup):

        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        if self.lp.login_status() == True:
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\OrangeHRMPro\\ScreenShot\\test_login_002_Pass.png")
            self.lp.click_menu()
            self.lp.click_logout()

            assert True

        else:
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\OrangeHRMPro\\ScreenShot\\test_login_002_Fail.png")
            assert False
        self.driver.close()
