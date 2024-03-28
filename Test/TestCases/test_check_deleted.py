from Test.Config import config
from Test.PageObjectModels import ViewBlogPageObject
import time
import pytest
class TestCheckDeleted:
    """
        Steps:
            1. Initialize driver and necessary page objects.
            2. Wait for a certain duration to ensure deletion process completes.
            3. Assert if the comment is deleted successfully.
            4. Perform teardown actions.
        """
    @pytest.mark.run(order=5)
    def test_check_deleted(self, openBrowser):
        self.driver = openBrowser
        self.config = config.ConfigClass(self.driver)
        self.vbp = ViewBlogPageObject.ViewBlogPageClass(self.driver)
        time.sleep(3)
        assert self.vbp.is_comment_deleted()
        time.sleep(2)
        self.config.tearDown()
