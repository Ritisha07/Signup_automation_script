from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import StaleElementReferenceException

class AgreementPage(BasePage):
    I_AGREE_CHECKBOX = (By.ID, "remember")  
    CONTINUE_BTN = (By.XPATH, "//button[text()='Continue']")  

    def continueNext(self):
        wait = WebDriverWait(self.driver, 10)

        for _ in range(3):  
            try:
                checkbox = wait.until(EC.element_to_be_clickable(self.I_AGREE_CHECKBOX))
                checkbox.click()
                break
            except StaleElementReferenceException:
                continue 

       
        for _ in range(3):
            try:
                continue_btn = wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
                continue_btn.click()
                break
            except StaleElementReferenceException:
                continue
