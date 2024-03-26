import time
import pytest
from Test.PageObjectModels import LoginPageObject
from Test.PageObjectModels import HomePageObject
from Test.PageObjectModels import PostingPageObject
from Test.Config import config

class TestAddPost:

    @pytest.mark.run(order=1)
    def test_adding_post(self,openBrowser):
        self.driver = openBrowser
        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)
        self.pp = PostingPageObject.PostingPageClass(self.driver)

        self.config.set_by_url(config.main_URL)
        assert self.lp.isSignInEnabled()
        self.lp.clickSignIn()
        time.sleep(3)
        self.lp.applyLogin(self.lp.admin_mail, self.lp.admin_password)
        time.sleep(3)
        assert self.hp.isLoginSuccessful()

        self.hp.clickNewPost()
        time.sleep(3)
        self.pp.applyPosting()
        time.sleep(3)
        assert self.hp.isLoginSuccessful()
        self.config.tearDown()




