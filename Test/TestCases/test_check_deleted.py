from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Test.PageObjectModels import LoginPageObject, CommentsPageObject, ViewBlogPageObject
from Test.PageObjectModels import HomePageObject
from selenium.webdriver.common.by import By
import time
import pytest

class TestCheckDeleted:

    @pytest.mark.run(order=5)
    def test_check_deleted(self):
            serv_obj = Service("C:\Drivers\chromedriver_win64\chromedriver-win64\chromedriver.exe")
            self.driver = webdriver.Chrome(service=serv_obj)
            self.driver.get("https://killeryodanttdata.blogspot.com/")
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.vbp = ViewBlogPageObject.ViewBlogPageClass(self.driver)
            time.sleep(3)
            assert self.vbp.is_comment_deleted()
            time.sleep(2)
            self.driver.quit()
