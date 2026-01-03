import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config import BASE_URL
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.agree_page import AgreementPage
from pages.signup_detail_page import SignupDetailsPage
from pages.otp_page import OTPPage

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
    
    
