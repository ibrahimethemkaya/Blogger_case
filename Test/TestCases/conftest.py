import logging
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service


# class Confest(unittest.TestCase): #log atmaya yarar
@pytest.fixture()
def openBrowser():
    serv_obj = Service("C:\Drivers\chromedriver_win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver


def loggerInit(self, name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(filename="test_log", mode="w")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
