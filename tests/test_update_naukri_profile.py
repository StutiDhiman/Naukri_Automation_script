import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

load_dotenv()

def test_update_resume(driver):
    email = os.getenv("NAUKRI_EMAIL")
    password = os.getenv("NAUKRI_PASSWORD")
    resume_path = os.getenv("RESUME_PATH")

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(email, password)

    profile_page = ProfilePage(driver)
    profile_page.navigate()
    profile_page.upload_resume(resume_path)
