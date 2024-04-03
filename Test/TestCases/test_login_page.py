import pytest

from Test.PageObjectModels import LoginPageObject, HomePageObject
import time
from Test.Config import config
from Test.TestCases.conftest import loggerInit


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
    @pytest.mark.run(order=1)
    def test_login(self, openBrowser):
        self.logger = loggerInit(self, self.__class__.__name__)
        self.logger.info("test starting---")

        self.logger.info("Initializing browser...")
        self.driver = openBrowser

        self.logger.info("Initializing configuration...")
        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)

        self.logger.info("Setting configuration URL...")
        self.config.set_by_url(config.main_URL)
        self.logger.info("Checking if sign-in is enabled...")
        assert self.lp.isSignInEnabled()
        self.logger.info("Clicking on sign-in button...")
        self.lp.clickSignIn()
        time.sleep(3)
        self.logger.info("Applying login credentials...")
        self.lp.applyLogin(self.lp.admin_mail, self.lp.admin_password)
        time.sleep(3)
        self.logger.info("Verifying login success...")
        assert self.hp.isLoginSuccessful()
        self.logger.info("Performing teardown...")
        self.config.tearDown()
        self.logger.info("Test Login completed successfully.")
