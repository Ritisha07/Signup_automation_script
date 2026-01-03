from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    SIGNUP_LINK = (By.XPATH, "//a[text()='Sign Up']")

    def go_to_signup(self):
        self.click(self.SIGNUP_LINK)
