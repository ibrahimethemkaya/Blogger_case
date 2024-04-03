import pyperclip
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class PostingPageClass:

    #Locators
    button_select_ID = "picker:ap:0"
    button_publish_CSS = "div[aria-label='Publish'] span[class='CwaK9']"
    button_confirm_xpath = "(//span[@class='RveJvd snByac'][normalize-space()='Confirm'])[2]"
    button_select_image_xpath = "//div[@class='kKlVTb']//div[@class='CQapMb']"
    button_by_Url_CSS = "div[class='JPdR6b e5Emjc qjTEB'] span[aria-label='By URL']"

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

    def click_select_image(self):
        self.driver.find_element(By.XPATH, self.button_select_image_xpath).click()

    def click_by_Url(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_by_Url_CSS).click()

    def send_url(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/iframe"))
        txtbox_url = self.driver.find_element(By.ID, ":c")
        pyperclip.copy("https://i.etsystatic.com/40317824/r/il/1fc564/4850621406/il_794xN.4850621406_lxg6.jpg")
        txtbox_url.send_keys(Keys.CONTROL, 'v')

    def applyPosting(self):
        self.click_select_image()
        time.sleep(3)
        self.click_by_Url()
        time.sleep(3)
        self.send_url()
        time.sleep(3)
        self.clickSelectBtn()
        time.sleep(3)
        self.clickPublishBtn()
        time.sleep(3)
        self.clickConfirmBtn()
