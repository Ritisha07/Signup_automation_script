from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AgencyPage(BasePage):
    NAME = (By.NAME, "agency_name")
    ROLE = (By.NAME, "role_in_agency")
    EMAIL = (By.NAME, "agency_email")
    WEBSITE = (By.NAME, "agency_website")
    ADDRESS = (By.NAME, "agency_address")
    REGION_DROPDOWN = (By.XPATH,"//label[normalize-space()='Region of Operation']/following-sibling::button")
    REGION_OPTION = "//div[contains(@class,'cursor-pointer') and span[normalize-space()='{}']]"
    NEXT_BTN = (By.XPATH, "//button[normalize-space()='Next']")

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.NAME))

    def fill_agency_details(
        self, name, role, email, website, address, regions: list
    ):
        self.send_keys(self.NAME, name)
        self.send_keys(self.ROLE, role)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.WEBSITE, website)
        self.send_keys(self.ADDRESS, address)

        
        self.click(self.REGION_DROPDOWN)

        
        for region in regions:
            option = (By.XPATH, self.REGION_OPTION.format(region))
            self.wait.until(EC.element_to_be_clickable(option)).click()

        self.click(self.NEXT_BTN)
