from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.agree_page import AgreementPage
from pages.signup_detail_page import SignupDetailsPage
from pages.otp_page import OTPPage
from pages.agency_detail_page import AgencyPage
from pages.verification_page import VerificationPage
from pages.experience_page import ExperiencePage

def test_full_signup_flow(driver):
    home = HomePage(driver)
    home.go_to_login()

    login = LoginPage(driver)
    login.go_to_signup()

    agree = AgreementPage(driver)
    agree.continueNext()

    signup_detail = SignupDetailsPage(driver)
    signup_detail.fill_signup_details(
        fname="Rpp",
        lname="sss",
        email="viyiy96545@cucadas.com",
        phone="9800011456",
        password="Ritisha01#",
        confirm_password="Ritisha01#"
        
    )
    # the otp should add manually 
        
    otp_page = OTPPage(driver)
    print("Please enter OTP manually in the browser...")
    otp_page.wait_for_manual_otp_entry()
    
    print("OTP entered and verified. Continuing with the rest of the test...")


    agency = AgencyPage(driver)
    agency.wait_until_loaded()
    agency.fill_agency_details(
        name="Vrit Tech",
        role="QA Engineer",
        email="info@vrittech.com",
        website="example.com",
        address="Kathmandu",
        regions=["Australia", "Canada"] 
    )
    
    experience = ExperiencePage(driver)
    experience.fill_experience_section(
        experience_level="5 years",
        num_students=120,
        focus_area="Automation Testing",
        success_metrics="20",
        services=["Career Counseling","Visa Processing"]
    )
    
    
    verification = VerificationPage(driver) 
    verification.complete_verification(
        reg_no="BRN-2025-XYZ",
        countries=["Australia", "Canada"],   
        institutions=["Universities", "Colleges"],     
        certification="ISO 9001 Certified",
        file_path=r"C:\Users\Ritisha\Desktop\Ritisha Resume\aa.pdf"
    )

    