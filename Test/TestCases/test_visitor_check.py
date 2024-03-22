from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Test.PageObjectModels import LoginPageObject, VisitorPageObject
from Test.PageObjectModels import HomePageObject
from Test.PageObjectModels import PostingPageObject
from selenium.webdriver.common.by import By
import time
import pytest

class TestVisitorCheck:

    @pytest.mark.run(order=3)
    def test_visitor_check(self):
        serv_obj = Service("C:\Drivers\chromedriver_win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.get("https://killeryodanttdata.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.vp = VisitorPageObject.VisitorPageClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        assert self.vp.isCommentVisible()

        self.vp.clickCommendBtn()
        self.vp.clickSignIn()
        self.lp.sendMail("visitor.bloggercase@gmail.com")
        time.sleep(3)
        self.lp.clickNext()
        time.sleep(3)
        self.lp.sendPassword("bloggervisitor123")
        time.sleep(3)
        self.lp.clickNext()
        time.sleep(5)
        self.vp.sendCommendMessage()
        time.sleep(1)
        self.driver.quit()






