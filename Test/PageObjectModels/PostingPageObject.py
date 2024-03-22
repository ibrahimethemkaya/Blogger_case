import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class PostingPageClass:
    # admin_mail : blogger.for.test.ntt@gmail.com
    # password : Downloading456.

    #Locators
    button_select_ID = "picker:ap:0"
    button_publish_CSS = "div[aria-label='Publish'] span[class='CwaK9']"
    button_confirm_xpath = "(//span[@class='RveJvd snByac'][normalize-space()='Confirm'])[2]"

    #constructor
    def __init__(self,driver):
        self.driver = driver


    # action methods

    def clickSelectBtn(self):
        self.driver.find_element(By.ID,self.button_select_ID).click()

    def clickPublishBtn(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_publish_CSS).click()

    def clickConfirmBtn(self):
        self.driver.find_element(By.XPATH,self.button_confirm_xpath).click()
