import pyperclip
import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

class CommentsPageClass:
    # Locators
    comments_class = "LgQiCc"



    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def isCommentVisible(self):
        elements = self.driver.find_elements(By.CLASS_NAME,self.comments_class)
        if not elements:
            return False
        else : return True

    def commentDeleteIcon(self):
        action = ActionChains(self.driver)
        delete_icon_area = self.driver.find_element(By.XPATH,"(//div[@class='opmHNc'])[1]")
        action.move_to_element(delete_icon_area).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//c-wiz[@class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e']//div[@role='list']//div[1]//span[1]//div[1]//div[1]//div[4]//div[3]//span[1]//span[1]//span[1]").click()
        time.sleep(2)

    def commentDeleteButton(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[aria-label='Delete this comment and its replies']").click()
