import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.RequirementPage import RequirementPage
from utilities.customLogger import LogGen
from base.test_BasePage import Test_Base



class Test_VRMCSB(Test_Base):
    logger = LogGen.loggen()

    def test_req_matching_candidate_search(self,driver):
            time.sleep(1)
            self.logger.info("******* Test_Base *******")
            self.driver = driver
            self.logger.info("===== Starting Requirement Search Test =====")

            requirement_page = RequirementPage(self.driver)

            # Test steps
            time.sleep(1)
            requirement_page.click_requirement_tab()
            self.logger.info("Clicked Requirement tab")

            requirement_page.click_matching_positions()
            self.logger.info("Clicked Requirement tab")

            search_text="PRIYA SHARMA"
            requirement_page.type_search_resources(search_text)

            actual_text=requirement_page.get_search_result()
            self.logger.info(f"Entered search text: {search_text}")
            time.sleep(1)

            if actual_text == "PRIYA SHARMA":
                print("Search bar is working")
            else:
                print("Search bar is NOT working")

            time.sleep(1)
            requirement_page.click_cancel()
            time.sleep(1)


