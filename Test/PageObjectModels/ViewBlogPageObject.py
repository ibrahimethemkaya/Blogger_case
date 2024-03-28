import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ViewBlogPageClass:


    #Locators
    button_comments_class = "num_comments"



    #constructor
    def __init__(self,driver):
        self.driver = driver



    #action methods

    def is_comment_deleted(self):
        if self.driver.find_element(By.CLASS_NAME, self.button_comments_class).text.__contains__('Post'):
            return True
        else:
            return False