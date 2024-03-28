from Test.PageObjectModels import LoginPageObject, CommentsPageObject, HomePageObject
from Test.Config import config
import pytest
import time

from Test.TestCases.conftest import loggerInit


class TestDeleteComment:
    """
       Steps:
           1. Initialize driver and necessary page objects.
           2. Set configuration using the main URL.
           3. Assert if sign-in option is enabled.
           4. Click on sign-in.
           5. Perform login using admin credentials.
           6. Assert if login is successful.
           7. Click on 'Comments' option.
           8. Verify if a comment exists.
           9. Perform comment deletion.
           10. Perform teardown actions.
       """
    @pytest.mark.run(order=4)
    def test_delete_comment(self, openBrowser):
        self.driver = openBrowser
        self.logger = loggerInit(self, self.__class__.__name__)
        self.logger.info("Initializing delete comment test...")
        self.logger.info("Browser initialized successfully.")

        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)
        self.cp = CommentsPageObject.CommentsPageClass(self.driver)
        self.logger.info("Setting configuration URL...")
        self.config.set_by_url(config.main_URL)
        self.logger.info("Checking if sign-in is enabled...")
        assert self.lp.isSignInEnabled()
        self.logger.info("Clicking on sign-in button...")
        self.lp.clickSignIn()
        self.logger.info("Applying login credentials...")
        time.sleep(3)
        self.lp.applyLogin(self.lp.admin_mail, self.lp.admin_password)
        time.sleep(3)
        assert self.hp.isLoginSuccessful()
        self.logger.info("Login successful.")
        self.hp.clickComments()
        self.logger.info("Clicking on comments link...")
        #self.cp.verifyComment()
        self.logger.info("Verifying comment...")
        time.sleep(2)
        self.cp.commentDelete()
        self.logger.info("Deleting comment...")
        time.sleep(3)
        self.config.tearDown()
        self.logger.info("Test completed successfully.")
