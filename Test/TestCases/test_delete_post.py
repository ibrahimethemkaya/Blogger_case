import pytest
import time
from Test.Config import config
from Test.PageObjectModels import LoginPageObject, HomePageObject
from Test.TestCases.conftest import loggerInit


class TestDeletePost:
    """
       Steps:
           1. Initialize driver and necessary page objects.
           2. Set configuration using the main URL.
           3. Assert if sign-in option is enabled.
           4. Click on sign-in.
           5. Perform login using admin credentials.
           6. Assert if login is successful.
           7. Click on last post' deletion icon and approve it.
           8. Wait for a certain duration.
           9. Perform teardown actions.
       """
    @pytest.mark.run(order=6)
    def test_delete_post(self, openBrowser):
        self.logger = loggerInit(self, self.__class__.__name__)
        self.driver = openBrowser
        self.logger.info("Initializing delete post test...")
        self.logger.info("Browser initialized successfully.")
        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)

        self.config.set_by_url(config.main_URL)
        self.logger.info("Checking if sign-in is enabled...")
        assert self.lp.isSignInEnabled()
        self.lp.clickSignIn()
        self.logger.info("Clicking on sign-in button...")
        time.sleep(3)
        self.logger.info("Applying login credentials...")
        self.lp.applyLogin(self.lp.admin_mail, self.lp.admin_password)
        time.sleep(3)
        assert self.hp.isLoginSuccessful()
        self.logger.info("Login successful.")
        self.hp.clickDeleteLastPost()
        self.logger.info("Clicking to delete the last post...")
        time.sleep(2)
        self.config.tearDown()
        self.logger.info("Test completed successfully.")
