main_URL = "https://www.blogger.com/about/?bpli=1"
visitor_URl = "https://killeryodanttdata.blogspot.com/"
class ConfigClass:

    def __init__(self, driver):
        self.driver = driver

    def set_by_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()