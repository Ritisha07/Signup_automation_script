from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OTPPage:
    OTP_INPUTS = (By.CSS_SELECTOR, "input[data-input-otp='true']")
    VERIFY_BTN = (By.XPATH, "//button[normalize-space()='Verify Code']")

    def __init__(self, driver,timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    def wait_for_manual_otp_entry(self):
        otp_boxes = self.wait.until(EC.visibility_of_all_elements_located(self.OTP_INPUTS))

        all_filled = False
        while not all_filled:
            all_filled = all(box.get_attribute("value") for box in otp_boxes)
        self.wait.until(EC.element_to_be_clickable(self.VERIFY_BTN)).click()
        
        
    