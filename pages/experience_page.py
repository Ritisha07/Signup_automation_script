from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class ExperiencePage(BasePage):
    EXPERIENCE_SELECT = (By.XPATH, "//select[@aria-hidden='true']")
    NUM_STUDENTS = (By.NAME, "number_of_students_recruited_annually")
    FOCUS_AREA = (By.NAME, "focus_area")
    SUCCESS_METRICS = (By.NAME, "success_metrics")
    # SERVICE_CHECKBOX = (By.XPATH, "//button[@type='button' and @class='font-medium']")
    SERVICE_CHECKBOX_XPATH = "//label[normalize-space()='{}']/preceding-sibling::button[@role='checkbox']"

    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Next']")

    def select_experience_level(self, years_text: str):
       select_el = self.wait.until(lambda d: d.find_element(*self.EXPERIENCE_SELECT))
       Select(select_el).select_by_visible_text(years_text)

    def select_services(self, services: list):
        for service in services:
                xpath = self.SERVICE_CHECKBOX_XPATH.format(service)
                checkbox = self.wait.until(lambda d: d.find_element(By.XPATH, xpath))
                
                if checkbox.get_attribute("aria-checked") == "false":
                    checkbox.click()


    def fill_experience_section(self, experience_level, num_students, focus_area, success_metrics, services):
        self.select_experience_level(experience_level)
        self.send_keys(self.NUM_STUDENTS, str(num_students))
        self.send_keys(self.FOCUS_AREA, focus_area)
        self.send_keys(self.SUCCESS_METRICS, success_metrics)
        self.select_services(services)
        self.click(self.NEXT_BUTTON)
