import pyperclip
import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

class HomePageClass:
    # Locators
    button_new_post_CSS = "c-wiz[class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e'] div[class='Iun9']"
    posts_last_class = "gNK4lf"
    button_comments_CSS = "c-wiz[class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e'] span[aria-label='Comments'] div[class='kurlme DQGx6d']"
    button_update_CSS = "div[aria-label='Update'] span[class='CwaK9']"
    frame_className = "ZW3ZFc"
    textbox_className = "editable"
    comment_text = " This is Killer Yoda"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def clickNewPost(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_new_post_CSS).click()
    def isLoginSuccessful(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.button_new_post_CSS).is_enabled()

    def clickLastPost(self):
        elements = self.driver.find_elements(By.CLASS_NAME,self.posts_last_class)
        if elements[0].is_enabled():
            elements[0].click()

    def edit_post(self):
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, self.frame_className))
        time.sleep(2)
        textbox_edit = self.driver.find_element(By.CLASS_NAME, self.textbox_className)
        time.sleep(2)
        pyperclip.copy(self.comment_text)
        textbox_edit.send_keys(Keys.CONTROL, 'v')
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,self.button_update_CSS).click()

    def applyEdit(self):
        self.clickLastPost()
        time.sleep(3)
        self.edit_post()
        time.sleep(3)

    def is_update_enabled(self):
        status = self.driver.find_element(By.CSS_SELECTOR,self.button_update_CSS).is_enabled()
        return status
    def click_publish(self):
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "ZW3ZFc"))

    def clickComments(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_comments_CSS).click()

    def getPostCount(self):
      str = self.driver.find_element(By.CSS_SELECTOR,"div[class='MocG8c iRqe nj0FMe F8KQq LMgvRb KKjvXb'] span[class='vRMGwf oJeWuf']").text
      elements = str.split()
      return int(elements[1])

    def clickDeleteLastPost(self):
        action = ActionChains(self.driver)
        delete_post_area = self.driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div[1]/div")
        action.move_to_element(delete_post_area).perform()

        self.driver.find_element(By.XPATH,"(//span[@class='DPvwYc'][contains(text(),'')])[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//span[@class='RveJvd snByac'][normalize-space()='Trash post'])[2]").click()
        time.sleep(2)

    def countAfterDeleted(self):
      str = self.driver.find_element(By.CSS_SELECTOR,"div[class='MocG8c iRqe nj0FMe F8KQq LMgvRb KKjvXb'] span[class='vRMGwf oJeWuf']").text
      elements = str.split()
      return int(elements[1])
