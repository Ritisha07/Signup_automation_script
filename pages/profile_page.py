from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ProfilePage(BasePage):
    PROFILE_HEADER = (By.XPATH, "//h2[normalize-space()='My Profile']")
    # OR
    # EDIT_PROFILE_BTN = (By.XPATH, "//button[normalize-space()='Edit Profile']")

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.PROFILE_HEADER))
