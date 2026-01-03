from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class VerificationPage(BasePage):
    REG_NO = (By.NAME, "business_registration_number")
    COUNTRY_DROPDOWN = (By.XPATH, "//button[@role='combobox' and .//span[contains(text(),'Select Your Preferred Countries')]]")
    COUNTRY_OPTION = "//div[contains(@class,'cursor-pointer') and span[normalize-space()='{}']]"

    CERTIFICATION = (By.NAME, "certification_details")
    INSTITUTION_CHECKBOX = ("//label[normalize-space()='Universities']/preceding-sibling::button[@role='checkbox']")
    INSTITUTION_CHECKBOX = "//label[normalize-space()='{}']/preceding-sibling::button[@role='checkbox']"
    FILE_UPLOAD = (By.XPATH, "//input[@type='file']")
    NEXT_BTN = (By.XPATH, "//button[normalize-space()='Submit']")

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.REG_NO))

    def enter_business_reg_no(self, reg_no: str):
        """Wait for field to be visible before typing"""
        element = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.REG_NO)
        )
        element.clear()
        element.send_keys(reg_no)  
        
    def select_countries(self, countries: list):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.COUNTRY_DROPDOWN))
        dropdown.click()

        for country in countries:
            option_xpath = self.COUNTRY_OPTION.format(country)
            option_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, option_xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", option_element)
            self.driver.execute_script("arguments[0].click();", option_element)

        dropdown.click()
        
    def select_institution_types(self, institutions: list):
        for inst in institutions:
            checkbox = (By.XPATH, self.INSTITUTION_CHECKBOX.format(inst))
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(checkbox)  
            )
            
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(checkbox)
            )

            if element.get_attribute("aria-checked") == "false":
                element.click()

    def enter_certification(self, certification: str):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CERTIFICATION)
        )
        element.clear()
        element.send_keys(certification)

    def upload_business_document(self, file_path: str):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FILE_UPLOAD)
        )
        element.send_keys(file_path)

    def click_next(self):
        self.wait.until(EC.element_to_be_clickable(self.NEXT_BTN)).click()

    def complete_verification(self, reg_no, countries, certification, institutions, file_path):
        self.enter_business_reg_no(reg_no)
        self.select_countries(countries)
        self.select_institution_types(institutions)
        self.enter_certification(certification)
        self.upload_business_document(file_path)
        self.submit_and_wait_for_profile()
    
    def submit_and_wait_for_profile(self):
        self.click_next()

        # Wait for URL change OR profile element
        WebDriverWait(self.driver, 20).until(
            EC.url_contains("profile")
        )

