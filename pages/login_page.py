from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    EMAIL = (By.ID, "usernameField")
    PASSWORD = (By.ID, "passwordField")
    SUBMIT = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.naukri.com/mnjuser/login")

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.EMAIL))
        self.driver.find_element(*self.EMAIL).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PASSWORD))
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUBMIT))
        self.driver.find_element(*self.SUBMIT).click()
        time.sleep(4)
