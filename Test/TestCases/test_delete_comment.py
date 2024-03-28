from Test.PageObjectModels import LoginPageObject, CommentsPageObject, HomePageObject
from Test.Config import config
import pytest
import time


class TestDeleteComment:

    @pytest.mark.run(order=4)
    def test_delete_comment(self, openBrowser):
        self.driver = openBrowser

        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)
        self.cp = CommentsPageObject.CommentsPageClass(self.driver)

        self.config.set_by_url(config.main_URL)
        assert self.lp.isSignInEnabled()
        self.lp.clickSignIn()
        time.sleep(3)
        self.lp.applyLogin(self.lp.admin_mail, self.lp.admin_password)
        time.sleep(3)
        assert self.hp.isLoginSuccessful()
        self.hp.clickComments()
        self.cp.verifyComment()
        time.sleep(2)
        self.cp.commentDelete()
        time.sleep(3)
        self.config.tearDown()
