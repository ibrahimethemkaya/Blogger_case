from Test.PageObjectModels import LoginPageObject,HomePageObject,PostingPageObject
import time
import pytest
from Test.Config import config
from Test.TestCases.conftest import loggerInit


class TestAddpost:
    """
        Steps:
            1. Initialize driver and necessary page objects.
            2. Set configuration using the main URL.
            3. Assert if sign-in option is enabled.
            4. Click on sign-in.
            5. Perform login using admin credentials.
            6. Assert if login is successful.
            7. Apply editing operation on the home page.
            8. Assert if update option is enabled.
            9. Perform teardown actions.
        """
    @pytest.mark.run(order=2)
    def test_adding_post(self,openBrowser):
        self.logger = loggerInit(self, self.__class__.__name__)
        self.logger.info("Initializing Edit Post Test...")
        self.driver = openBrowser
        self.logger.info("Browser initialized successfully.")
        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)

        self.logger.info("Setting configuration URL...")
        self.config.set_by_url(config.main_URL)
        assert self.lp.isSignInEnabled()
        self.logger.info("Checking if sign-in is enabled...")
        self.lp.clickSignIn()
        self.logger.info("Clicking on sign-in button...")
        time.sleep(3)
        self.logger.info("Applying login credentials...")
        self.lp.applyLogin(self.lp.admin_mail, self.lp.admin_password)
        time.sleep(3)
        self.logger.info("Verifying login success...")
        assert self.hp.isLoginSuccessful()
        self.logger.info("Verifying if update is enabled after edit...")
        self.hp.applyEdit()
        assert self.hp.is_update_enabled()
        self.logger.info("Test completed successfully.")
        self.config.tearDown()






