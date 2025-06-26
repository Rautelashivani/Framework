import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.BenchPage import BenchPage
from utilities.customLogger import LogGen
from base.test_BasePage import Test_Base



class Test_VB(Test_Base):
    logger = LogGen.loggen()

    def test_tech_stack_search(self,driver):
            time.sleep(1)
            self.logger.info("******* Test_Base *******")
            self.driver = driver
            self.logger.info("===== Starting Tech Stack Search Test =====")

            bench_page = BenchPage(self.driver)

            # Test steps
            time.sleep(1)
            bench_page.click_bench_tab()
            self.logger.info("Clicked Bench tab")

            time.sleep(1)
            bench_page.click_tech_stack()
            self.logger.info("Clicked Tech Stack button")

            time.sleep(1)
            search_text = "JIRA"
            bench_page.search_tech_stack(search_text)
            self.logger.info(f"Entered search text: {search_text}")
            time.sleep(1)

            actual_text = bench_page.get_jira_result_text()
            if actual_text == "JIRA":
                    print("Search bar is working")
            else:
                    print("Search bar is NOT working")
