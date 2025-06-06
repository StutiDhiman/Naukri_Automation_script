from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        time.sleep(4)
        self.driver.get("https://www.naukri.com/mnjuser/profile")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    def upload_resume(self, resume_path):
        upload_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        upload_input.send_keys(resume_path)
        time.sleep(4)
