from Test.PageObjectModels import LoginPageObject, VisitorPageObject,HomePageObject
from Test.Config import config
import time
import pytest

from Test.TestCases.conftest import loggerInit


class TestVisitorCheck:
    """
       Steps:
           1. Initialize driver and necessary page objects.
           2. Set configuration using the visitor URL.
           3. Assert if the visitor page is displayed.
           4. Click on sign-in.
           5. Perform login using visitor credentials.
           6. Assert if comments are visible.
           7. Send a comment message.
           8. Perform teardown actions.
       """
    @pytest.mark.run(order=4)
    def test_visitor_check(self,openBrowser):
        self.logger = loggerInit(self, self.__class__.__name__)
        self.driver = openBrowser
        self.logger.info("Initializing visitor check test...")
        self.logger.info("Browser initialized successfully.")

        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)
        self.vp = VisitorPageObject.VisitorPageClass(self.driver)
        self.logger.info("Setting configuration URL...")

        self.logger.info("Checking if blog page is displayed...")
        self.config.set_by_url(config.visitor_URl)
        self.logger.info("Blog page is displayed.")
        assert self.vp.isBlogPageDisplayed()
        self.logger.info("Clicking on sign-in link...")
        self.vp.click_sign_in()
        self.logger.info("Applying login credentials...")
        self.lp.applyLogin(self.lp.visitor_mail, self.lp.visitor_password)
        self.logger.info("Sending comment message...")
        time.sleep(3)
        self.vp.sendCommentMessage()
        time.sleep(1)
        self.logger.info("Verifying if comment is visible...")
        assert self.vp.isCommentVisible()
        self.logger.info("Test completed successfully.")
        self.config.tearDown()






