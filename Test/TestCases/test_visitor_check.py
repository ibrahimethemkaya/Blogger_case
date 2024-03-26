from Test.PageObjectModels import LoginPageObject, VisitorPageObject,HomePageObject
from Test.Config import config
import time
import pytest

class TestVisitorCheck:

    @pytest.mark.run(order=3)
    def test_visitor_check(self,openBrowser):
        self.driver = openBrowser
        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)
        self.vp = VisitorPageObject.VisitorPageClass(self.driver)

        self.config.set_by_url(config.visitor_URl)
        assert self.lp.isSignInEnabled()
        self.vp.clickCommentBtn()
        self.vp.clickSignIn()
        self.lp.applyLogin(self.lp.visitor_mail, self.lp.visitor_password)
        time.sleep(3)
        assert self.hp.isLoginSuccessful()
        assert self.vp.isCommentVisible()
        self.vp.sendCommentMessage()
        time.sleep(1)
        self.config.tearDown()






