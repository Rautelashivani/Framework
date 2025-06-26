import time
import pytest
from pageObjects.BenchPage import BenchPage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen

from utilities.readProperties import ReadConfig


class Test_VBTSSB:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_tech_stack_search(self,driver):


            self.logger.info("******* Test_Base *******")
            self.logger.info("******* Opening Browser *******")
            self.driver = driver
            self.driver.get(self.baseURL)

            self.lp = LoginPage(self.driver)

            self.lp.setUserName(self.username)

            self.lp.setPassword(self.password)

            self.lp.clickLogin()
            time.sleep(2)


            self.logger.info("===== Starting Tech Stack Search Test =====")

            bench_page = BenchPage(self.driver)

            # Test steps
            time.sleep(2)
            bench_page.click_bench_tab()
            self.logger.info("Clicked Bench tab")

            time.sleep(2)
            bench_page.click_tech_stack()
            self.logger.info("Clicked Tech Stack button")

            time.sleep(2)
            search_text = "JIRA"
            bench_page.search_tech_stack(search_text)
            self.logger.info(f"Entered search text: {search_text}")

            # Verification
            time.sleep(2)
            self.lp.clickLogout()
       #     actual_text = bench_page.get_jira_result_text()
       #     assert actual_text == "JIRA", f"Expected 'JIRA' but got '{actual_text}'"
       #     self.logger.info("Search bar is working - JIRA found")


        #    self.logger.error(f"Test failed: {str(e)}")
         #   pytest.fail(f"Test failed: {str(e)}")


        #    self.logger.info("===== Test Completed =====")
        #    self.lp.clickLogout()