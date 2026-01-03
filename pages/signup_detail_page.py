from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SignupDetailsPage(BasePage):
    FIRST_NAME = (By.NAME, "firstName")          
    LAST_NAME = (By.NAME, "lastName")            
    EMAIL = (By.NAME, "email")                   
    PHONE = (By.NAME, "phoneNumber")                   
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirmPassword")
    NEXT_BTN = (By.XPATH, "//button[@type='submit' and text()='Next']")
  

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def fill_signup_details(self, fname, lname, email, phone, password, confirm_password):
        # Fill each field
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(fname)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(lname)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.PHONE)).send_keys(phone)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_PASSWORD)).send_keys(confirm_password)

    
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BTN)).click()
