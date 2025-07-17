import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.BenchPage import BenchPage
from utilities.customLogger import LogGen
from base.test_BasePage import Test_Base



class Test_VBMPSB(Test_Base):
    logger = LogGen.loggen()

    def test_bench_matching_positions_search(self,driver):
            time.sleep(1)
            self.logger.info("******* Test_Base *******")
            self.driver = driver
            self.logger.info("===== Starting Bench Matching Positions Search Test =====")

            bench_page = BenchPage(self.driver)

            # Test steps
            time.sleep(1)
            bench_page.click_bench_tab()
            self.logger.info("Clicked Bench tab")

            time.sleep(1)
            bench_page.click_matching_positions()
            self.logger.info("Clicked on Matching Positions")

            time.sleep(1)
            search_text = "Java Developer"
            bench_page.type_matching_search(search_text)
            self.logger.info(f"Entered search text: {search_text}")
            time.sleep(1)

            actual_text = bench_page.get_matching_result()
            if actual_text == "Java Developer":
                    print("Search bar is working")
            else:
                    print("Search bar is NOT working")

            time.sleep(2)
            bench_page.click_cancel_button()
            time.sleep(2)

