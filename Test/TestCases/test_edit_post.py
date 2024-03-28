from Test.PageObjectModels import LoginPageObject,HomePageObject,PostingPageObject
import time
import pytest
from Test.Config import config

class TestAddpost:

    @pytest.mark.run(order=2)
    def test_adding_post(self,openBrowser):
        self.driver = openBrowser
        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)

        self.config.set_by_url(config.main_URL)
        assert self.lp.isSignInEnabled()
        self.lp.clickSignIn()
        time.sleep(3)
        self.lp.applyLogin(self.lp.admin_mail, self.lp.admin_password)
        time.sleep(3)
        assert self.hp.isLoginSuccessful()
        self.hp.applyEdit()
        assert self.hp.is_update_enabled()  #bu kısmı sor
        self.config.tearDown()
        self.logger.info





