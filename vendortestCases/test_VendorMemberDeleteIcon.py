import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.MemberPage import MemberPage
from utilities.customLogger import LogGen
from base.test_BasePage import Test_Base



class Test_VMDI(Test_Base):
    logger = LogGen.loggen()

    def test_member_delete_icon(self,driver):
            time.sleep(1)
            self.logger.info("******* Test_Base *******")
            self.driver = driver
            self.logger.info("===== Starting Member delete icon Test =====")

            member_page=MemberPage(self.driver)

            # Test steps
            time.sleep(1)
            member_page.click_member_tab()
            self.logger.info("Clicked Member tab")
            time.sleep(2)


            member_page.delete_member()
            self.logger.info("Move to the name")
            self.logger.info("Click on Delete the member")



            member_page.click_delete_button()
            self.logger.info("Member is deleted")
            print("Member is deleted")

            time.sleep(2)





