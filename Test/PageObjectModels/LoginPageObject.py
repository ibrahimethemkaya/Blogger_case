import time
from selenium.webdriver.common.by import By


class LoginPageClass:
    # Locators
    admin_mail = "blogger.for.test.ntt@gmail.com"
    admin_password = "Downloading456."
    visitor_mail = "guestautomated1@gmail.com"
    visitor_password = "Guest123"
    button_sign_in_TAG = "span"
    textbox_mail_password_class = "whsOnd"
    button_next_xpath = "//span[normalize-space()='Next']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    def clickSignIn(self):
        # Clicks on the sign-in button.
        self.driver.find_element(By.TAG_NAME, self.button_sign_in_TAG).click()

    def isSignInEnabled(self):
        """
        Checks if the sign-in button is enabled.
        Returns:
        bool: True if sign-in button is enabled, False otherwise.
        """
        return self.driver.find_element(By.TAG_NAME, self.button_sign_in_TAG).is_enabled()

    def sendMail(self, mail):
        """
               Enters the email address into the email input field.

               Parameters:
                   mail (str): The email address to be entered.
        """
        self.driver.find_element(By.CLASS_NAME, self.textbox_mail_password_class).send_keys(mail)

    def clickNext(self):
        # Clicks on the 'Next' button during the login process.
        self.driver.find_element(By.XPATH, self.button_next_xpath).click()

    def sendPassword(self, password):
        """
               Enters the password into the password input field.

               Parameters:
                   password (str): The password to be entered.
        """
        self.driver.find_element(By.CLASS_NAME, self.textbox_mail_password_class).send_keys(password)

    def applyLogin(self, mail, password):
        # Performs the login operation by entering email, clicking 'Next', entering password, and clicking 'Next' again.
        self.sendMail(mail)
        time.sleep(3)
        self.clickNext()
        time.sleep(3)
        self.sendPassword(password)
        time.sleep(3)
        self.clickNext()
