import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class VisitorPageClass:
    # admin_mail : blogger.for.test.ntt@gmail.com
    # password : Downloading456.

    #Locators
    button_commend_class = "num_comments"
    frame_ID = "comment-editor"
    button_sign_in_xpath = "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div[1]"
    commend_ID = "FeaturedPost1"

    #constructor
    def __init__(self,driver):
        self.driver = driver

    def clickCommendBtn(self):
        self.driver.find_element(By.CLASS_NAME, self.button_commend_class).click()

    def clickSignIn(self):
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "comment-editor"))
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div[1]").click()
        self.driver.switch_to.default_content()

    def isCommentVisible(self):
        if self.driver.find_element(By.ID, self.commend_ID):
            return True
        else:
            return False


    def sendCommendMessage(self):
        self.driver.switch_to.frame(self.driver.find_element(By.ID, "comment-editor"))
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/div[2]/textarea")
        element.send_keys("this is not jedi, just a kid")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[3]/div[1]/div/span/span").click()
        self.driver.switch_to.default_content()
