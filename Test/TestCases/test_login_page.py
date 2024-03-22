import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Test.PageObjectModels import LoginPageObject
from Test.PageObjectModels import HomePageObject
from selenium.webdriver.common.by import By
import time
class TestLogin:
    @pytest.mark.skip
    def test_login(self):
            serv_obj = Service("C:\Drivers\chromedriver_win64\chromedriver-win64\chromedriver.exe")
            self.driver = webdriver.Chrome(service=serv_obj)
            self.driver.get("https://www.blogger.com/about/?bpli=1")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

            self.lp = LoginPageObject.LoginPageClass(self.driver)
            self.hp = HomePageObject.HomePageClass(self.driver)

            assert self.lp.isSignInEnabled()
            self.lp.clickSignIn()
            time.sleep(2)
            self.lp.sendMail("blogger.for.test.ntt@gmail.com")
            time.sleep(2)
            self.lp.clickNext()
            time.sleep(2)
            self.lp.sendPassword("Downloading456.")
            time.sleep(2)
            self.lp.clickNext()
            time.sleep(2)
            assert self.lp.isLoginSuccessful()


