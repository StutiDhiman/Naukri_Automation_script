
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_binary_path = "C:\\Users\\KUMAR\\Downloads\\chromedriver_win32\\chromedriver.exe"

def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()

email = os.getenv("NAUKRI_EMAIL")
password = os.getenv("NAUKRI_PASSWORD")
resume_path = os.getenv("RESUME_PATH")

print("hello")
driver = next(driver())
print("execution")

login_page = LoginPage(driver)
login_page.load()
login_page.login(email, password)

profile_page = ProfilePage(driver)
profile_page.navigate()
profile_page.upload_resume(resume_path)
