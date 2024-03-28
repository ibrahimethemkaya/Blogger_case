from Test.PageObjectModels import LoginPageObject, VisitorPageObject,HomePageObject
from Test.Config import config
import time
import pytest
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
    @pytest.mark.run(order=3)
    def test_visitor_check(self,openBrowser):
        self.driver = openBrowser

        self.config = config.ConfigClass(self.driver)
        self.lp = LoginPageObject.LoginPageClass(self.driver)
        self.hp = HomePageObject.HomePageClass(self.driver)
        self.vp = VisitorPageObject.VisitorPageClass(self.driver)

        self.config.set_by_url(config.visitor_URl)
        assert self.vp.isBlogPageDisplayed()
        self.vp.click_sign_in()
        self.lp.applyLogin(self.lp.visitor_mail, self.lp.visitor_password)
        time.sleep(3)
        self.vp.sendCommentMessage()
        time.sleep(1)
        assert self.vp.isCommentVisible()
        self.config.tearDown()






