import time
import pytest
from Test.PageObjectModels import LoginPageObject
from Test.PageObjectModels import HomePageObject
from Test.PageObjectModels import PostingPageObject
from Test.Config import config
from Test.TestCases.conftest import loggerInit


class TestAddPost:
    """
        Test method to verify the functionality of adding a new post.

        Parameters:
            openBrowser: A fixture providing an open browser instance.

        Steps:
            1. Initialize driver and necessary page objects.
            2. Set configuration using the main URL.
            3. Assert if sign-in option is enabled.
            4. Click on sign-in.
            5. Perform login using admin credentials.
            6. Assert if login is successful.
            7. Click on 'New Post' option.
            8. Apply posting operation.
            9. Assert posting is successful.
            10. Perform teardown actions.
        """
    @pytest.mark.run(order=1)
    def test_adding_post(self,openBrowser):
        self.driver = openBrowser
        self.logger = loggerInit(self, self.__class__.__name__)
        self.logger.info("Starting test_adding_post...")
        self.logger.info("Browser initialized successfully.")
        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)
        self.pp = PostingPageObject.PostingPageClass(self.driver)
        self.logger.info("Configurations initialized successfully.")

        self.config.set_by_url(config.main_URL)
        assert self.lp.isSignInEnabled()
        self.logger.info("Sign-in is enabled.")
        self.lp.clickSignIn()
        self.logger.info("Clicked on sign-in button.")
        time.sleep(3)
        self.lp.applyLogin(self.lp.admin_mail, self.lp.admin_password)
        self.logger.info("Applied login credentials.")
        time.sleep(3)
        assert self.hp.isLoginSuccessful()
        self.logger.info("Login successful.")

        self.hp.clickNewPost()
        self.logger.info("Clicked on new post button.")
        time.sleep(3)
        self.pp.applyPosting()
        self.logger.info("Applied posting.")
        time.sleep(3)
        assert self.hp.isLoginSuccessful()
        self.logger.info("Test completed successfully.")
        self.config.tearDown()




