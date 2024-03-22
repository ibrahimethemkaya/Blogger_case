import pyperclip
import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

class HomePageClass:
    # Locators
    button_new_post_CSS = "c-wiz[class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e'] div[class='Iun9']"
    button_select_image_xpath = "//div[@class='kKlVTb']//div[@class='CQapMb']"
    button_by_Url_CSS = "div[class='JPdR6b e5Emjc qjTEB'] span[aria-label='By URL']"
    posts_last_class = "gNK4lf"
    button_comments_CSS = "c-wiz[class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e'] span[aria-label='Comments'] div[class='kurlme DQGx6d']"



    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def clickNewPost(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_new_post_CSS).click()

    def click_select_image(self):
        self.driver.find_element(By.XPATH, self.button_select_image_xpath).click()

    def click_by_Url(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_by_Url_CSS).click()

    def send_url(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/iframe"))
        txtbox_url = self.driver.find_element(By.ID, ":c")
        pyperclip.copy("https://i.etsystatic.com/40317824/r/il/1fc564/4850621406/il_794xN.4850621406_lxg6.jpg")
        txtbox_url.send_keys(Keys.CONTROL, 'v')

    def clickLastPost(self):
        elements = self.driver.find_elements(By.CLASS_NAME,self.posts_last_class)
        elements[0].click()

    def edit_post(self):
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "ZW3ZFc"))
        time.sleep(2)
        txtbox_edit = self.driver.find_element(By.CLASS_NAME, "editable")
        time.sleep(2)
        pyperclip.copy(" this is killer yoda")
        txtbox_edit.send_keys(Keys.CONTROL, 'v')
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"div[aria-label='Update'] span[class='CwaK9']").click()

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
