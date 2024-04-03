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
    delete_post_area_xpath = "//*[@id='yDmH0d']/c-wiz/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div[1]/div"
    button_delete_post_xpath = "(//span[@class='DPvwYc'][contains(text(),'')])[2]"
    button_approve_delete_xpath = "(//span[@class='RveJvd snByac'][normalize-space()='Trash post'])[2]"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def clickNewPost(self):
        """
            Clicks on the 'New Post' button.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.button_new_post_CSS).click()

    def isLoginSuccessful(self):
        """
            Checks if the login is successful.

            Returns:
                bool: True if login is successful, False otherwise.
        """
        return self.driver.find_element(By.CSS_SELECTOR, self.button_new_post_CSS).is_enabled()

    def clickLastPost(self):
        """
            Clicks on the last post displayed.
        """
        elements = self.driver.find_elements(By.CLASS_NAME, self.posts_last_class)
        if elements[0].is_enabled():
            elements[0].click()

    def edit_post(self):
        """
               Steps:
                   1. Switch to the frame containing the post content.
                   2. Paste the edited content into the textbox.
                   3. Switch back to the default content.
                   4. Click on the 'Update' button.
        """
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, self.frame_className))
        time.sleep(2)
        textbox_edit = self.driver.find_element(By.CLASS_NAME, self.textbox_className)
        time.sleep(2)
        pyperclip.copy(self.comment_text)
        textbox_edit.send_keys(Keys.CONTROL, 'v')
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.button_update_CSS).click()

    def applyEdit(self):
        """
            Steps:
                1. Click on the last post.
                2. Edit the post.
        """
        self.clickLastPost()
        time.sleep(3)
        self.edit_post()
        time.sleep(3)

    def is_update_enabled(self):
        """
            Checks if the update status is enabled.

            Returns:
                bool: True if update status is enabled, False otherwise.
        """
        status = self.driver.find_element(By.XPATH, "//span[@title='Changes saved']").is_displayed()
        return status

    def click_publish(self):
        """
                Clicks on the publish button.
        """
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, "ZW3ZFc"))

    def clickComments(self):
        """
            Clicks on the 'Comments' button.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.button_comments_CSS).click()

    def clickDeleteLastPost(self):
        """
            Steps:
                1. Move to the delete post area using action chains.
                2. Click on the delete post button.
                3. Confirm the deletion by clicking on the approve delete button.
        """
        action = ActionChains(self.driver)
        delete_post_area = self.driver.find_element(By.XPATH, self.delete_post_area_xpath)
        action.move_to_element(delete_post_area).perform()

        self.driver.find_element(By.XPATH,self.button_delete_post_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.button_approve_delete_xpath).click()


