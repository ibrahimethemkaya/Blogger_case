import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPageClass:
    # admin_mail : blogger.for.test.ntt@gmail.com
    # password : Downloading456.
    # visitor_mail : visitor.bloggercase@gmail.com
    # pass = bloggervisitor123

    #Locators
    button_sign_in_TAG = "span"
    txtbox_mail_password_class= "whsOnd"
    button_next_xpath = "//span[normalize-space()='Next']"
    button_new_post_CSS = "c-wiz[class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e'] div[class='Iun9']"


    #constructor
    def __init__(self,driver):
        self.driver = driver

    #action methods
    def clickSignIn(self):
        self.driver.find_element(By.TAG_NAME, self.button_sign_in_TAG).click()

    def isSignInEnabled(self):
        return self.driver.find_element(By.TAG_NAME, self.button_sign_in_TAG).is_enabled()

    def isLoginSuccessful(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.button_new_post_CSS).is_enabled()

    def sendMail(self,mail):
        self.driver.find_element(By.CLASS_NAME, self.txtbox_mail_password_class).send_keys(mail)

    def clickNext(self):
        self.driver.find_element(By.XPATH, self.button_next_xpath).click()


    def sendPassword(self,password):
        self.driver.find_element(By.CLASS_NAME, self.txtbox_mail_password_class).send_keys(password)
    def clickNext(self):
        self.driver.find_element(By.XPATH, self.button_next_xpath).click()


