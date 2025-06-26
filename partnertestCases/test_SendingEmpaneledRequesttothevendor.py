import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from base.test_BasePage import Test_Base
from pageObjects.VendorPage import VendorPage
from utilities.customLogger import LogGen

from utilities.readProperties import ReadConfig



class Test_SERTV(Test_Base):

    logger = LogGen.loggen()

    def test_sending_empaneled_request(self,driver):
            time.sleep(1)
            self.logger.info("******* Test_Base *******")
            self.driver = driver
            self.logger.info("===== Starting sending empaneled request =====")


            vendor_page=VendorPage(self.driver)

            vendor_page.click_vendor_link()
            time.sleep(2)
            vendor_page.click_search_button()
            time.sleep(2)
            vendor_page.enter_search_text("Titoo")
            time.sleep(2)
            vendor_page.click_partner_vendor()
            time.sleep(2)
            vendor_page.click_empanelment_button()
            time.sleep(2)
            vendor_page.enter_message("hello")
            time.sleep(2)
            vendor_page.click_invite_button()
            time.sleep(4)

            # Verification
            act_output = vendor_page.get_actual_result()
            expected_output = "Invited successfully for Empanelment"

            if act_output == expected_output:
                print("Request has been sent")

            else:
                print("Request failed to send")

            time.sleep(4)



