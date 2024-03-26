import time
from selenium.webdriver.common.by import By

class LoginPageClass:

    admin_mail = "blogger.for.test.ntt@gmail.com"
    admin_password = "Downloading456."
    visitor_mail = "visitor.bloggercase@gmail.com"
    visitor_password = "bloggervisitor123"
    # Locators
    button_sign_in_TAG = "span"
    txtbox_mail_password_class = "whsOnd"
    button_next_xpath = "//span[normalize-space()='Next']"

    #constructor
    def __init__(self,driver):
        self.driver = driver

    #action methods
    def clickSignIn(self):
        self.driver.find_element(By.TAG_NAME, self.button_sign_in_TAG).click()

    def isSignInEnabled(self):
        return self.driver.find_element(By.TAG_NAME, self.button_sign_in_TAG).is_enabled()

    def sendMail(self,mail):
        self.driver.find_element(By.CLASS_NAME, self.txtbox_mail_password_class).send_keys(mail)

    def clickNext(self):
        self.driver.find_element(By.XPATH, self.button_next_xpath).click()

    def sendPassword(self,password):
        self.driver.find_element(By.CLASS_NAME, self.txtbox_mail_password_class).send_keys(password)

    def applyLogin(self,mail,password):
        self.sendMail(mail)
        time.sleep(3)
        self.clickNext()
        time.sleep(3)
        self.sendPassword(password)
        time.sleep(3)
        self.clickNext()

