from Test.PageObjectModels import LoginPageObject, HomePageObject
import time
from Test.Config import config


# -----TEST STEPS----
# Open the browser and visit blogger.com
# Verify if the sign-in button is enabled.
# Click on the sign-in button.
# Enter the admins email address.
# Click on the "Next" button.
# Enter the admins' password.
# Click on the "Next" button.
# Verify successful login.
# Tear down the test environment.

class TestLogin:

    def test_login(self, openBrowser):
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
        self.config.tearDown()
