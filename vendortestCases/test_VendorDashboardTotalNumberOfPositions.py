import time

import pytest

from base.test_BasePage import Test_Base
from pageObjects.DashboardPage import DashboardPage
from utilities.customLogger import LogGen


class Test_VDTNOP(Test_Base):
    logger = LogGen.loggen()


    def test_total_positions(self,driver):
        time.sleep(1)
        self.logger.info("******* Test_Base *******")
        self.driver = driver
        self.logger.info("===== Starting Total number of positions Test =====")

        dashboard_page=DashboardPage(self.driver)

        # Test steps
        time.sleep(1)

        header_value =dashboard_page.get_header_value()
        dashboard_page.click_header()
        sum_digits =dashboard_page.sum_numbers_before_parentheses()

        assert header_value == sum_digits, "Header value should match sum of positions"