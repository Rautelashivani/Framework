import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.SignupPage import SignupPage
from utilities.customLogger import LogGen

from utilities.readProperties import ReadConfig



class Test_AOWK:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_alert_on_weak_password(self,driver):

            self.logger.info("******* Test_Base *******")
            self.driver = driver
            self.logger.info("====opening the browser =====")
            self.driver.get(self.baseURL)
            self.logger.info("===== Starting Signup process =====")

            signup_page = SignupPage(self.driver)

            # Test steps
            time.sleep(1)
            signup_page.click_on_signup()
            self.logger.info("Clicked On signup")

            first_name="vendor"
            signup_page.type_first_name(first_name)
            self.logger.info("enter the first name")

            last_name="555"
            signup_page.type_last_name(last_name)
            self.logger.info("enter the last name")

            company_name="UKG"
            signup_page.type_company_name(company_name)
            self.logger.info("enter the company name")

            email_address="ukg@1yopcom"
            signup_page.type_email_address(email_address)
            self.logger.info("enter the email address")

            pass_word="123456"
            signup_page.type_pass_word(pass_word)
            self.logger.info("enter the password")

            time.sleep(2)

            alert_text = signup_page.get_alert()
            if alert_text == "Weak password (Use strong password)":
                print("Giving Alert")
                self.driver.save_screenshot(".\\Screenshots\\"+"test_alert_on_weak_password.png ")
            else:
                print("No Alert")

            signup_page.click_on_continue()
            self.logger.info("Clicked On continue")
