from Test.Config import config
from Test.PageObjectModels import ViewBlogPageObject
import time
import pytest

from Test.TestCases.conftest import loggerInit


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
        self.logger = loggerInit(self, self.__class__.__name__)
        self.logger.info("Initializing check deletion test...")

        self.driver = openBrowser
        self.logger.info("Browser initialized successfully.")
        self.config = config.ConfigClass(self.driver)
        self.vbp = ViewBlogPageObject.ViewBlogPageClass(self.driver)

        self.config.set_by_url(config.visitor_URl)
        time.sleep(2)
        assert self.vbp.is_comment_deleted()
        self.logger.info("Verifying if comment is deleted...")
        self.config.tearDown()
        self.logger.info("Test completed successfully.")
