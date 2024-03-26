import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture()
def openBrowser():
    serv_obj = Service("C:\Drivers\chromedriver_win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver