import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.PartnerPage import PartnerPage
from utilities.customLogger import LogGen
from base.test_BasePage import Test_Base



class Test_VPESB(Test_Base):
    logger = LogGen.loggen()

    def test_empaneled_search(self,driver):
            time.sleep(1)
            self.logger.info("******* Test_Base *******")
            self.driver = driver
            self.logger.info("===== Starting Empaneled Search Test =====")

            partner_page = PartnerPage(self.driver)

            # Test steps
            time.sleep(1)
            partner_page.click_partner_tab()
            self.logger.info("Clicked Partner tab")

            time.sleep(1)
            partner_page.click_empaneled_tab()
            self.logger.info("Clicked Empaneled tab")

            time.sleep(1)
            search_text = "IBM"
            partner_page.type_search_partner(search_text)
            self.logger.info(f"Entered search text: {search_text}")
            time.sleep(1)

            actual_text = partner_page.get_search_result()
            if actual_text == "IBM":
                print("Search bar is working")
            else:
                print("Search bar is NOT working")