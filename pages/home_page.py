from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://authorized-partner.vercel.app/"

    login_link = (By.CSS_SELECTOR, "a.px-4.flex.items-center.gap-2")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    def go_to_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_link)).click()
