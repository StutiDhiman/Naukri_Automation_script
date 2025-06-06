import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_binary_path = "C:\\Users\\KUMAR\\Downloads\\chromedriver_win32\\chromedriver.exe"

@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()