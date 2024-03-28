from selenium.webdriver import  ActionChains
from selenium.webdriver.common.by import By
import time

class CommentsPageClass:
    # Locators
    comments_class = "LgQiCc"
    comment_text = "this is not jedi, just a kid"
    delete_icon_area_xpath = "(//div[@class='opmHNc'])[1]"
    button_delete_icon_xpath = "//c-wiz[@class='zQTmif SSPGKf eejsDc qWnhY O3LMFb haXJ6e']//div[@role='list']//div[1]//span[1]//div[1]//div[1]//div[4]//div[3]//span[1]//span[1]//span[1]"
    button_delete_CSS = "div[aria-label='Delete this comment and its replies']"
    comment_xpath = ".//*[@class='Aknmsd ZtmlJb']//*[contains(text(), 'this is not jedi, just a kid')]"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def verifyComment(self):
        """
               Verifies if a specific comment is present on the page.

               Returns:
                   bool: True if the comment is found, False otherwise.
        """
        text = self.driver.find_element(By.XPATH,self.comment_xpath)[0].innerText
        return text == "this is not jedi, just a kid"

    def commentDelete(self):
        """
          Deletes a comment.

            Steps:
                1. Move to the delete icon area using action chains.
                2. Click on the delete icon.
                3. Confirm the deletion by clicking on the delete button.
        """
        action = ActionChains(self.driver)
        delete_icon_area = self.driver.find_element(By.XPATH, self.delete_icon_area_xpath)
        action.move_to_element(delete_icon_area).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button_delete_icon_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.button_delete_CSS).click()
