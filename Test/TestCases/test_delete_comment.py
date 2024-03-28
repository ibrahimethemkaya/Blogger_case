from Test.PageObjectModels import LoginPageObject, CommentsPageObject, HomePageObject
from Test.Config import config
import pytest
import time
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
        assert self.cp.verifyComment()
        time.sleep(2)
        self.cp.commentDelete()
        time.sleep(3)
        self.config.tearDown()
