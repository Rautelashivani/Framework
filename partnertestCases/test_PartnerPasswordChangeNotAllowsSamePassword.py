import time

from pageObjects.PartnerProfilePage import PartnerProfilePage
from utilities.customLogger import LogGen
from base.test_BasePage import Test_Base



class Test_PPCNASP(Test_Base):
    logger = LogGen.loggen()

    def test_password_change_not_allows_same_password(self,driver):
            time.sleep(1)
            self.logger.info("******* Test_Base *******")
            self.driver = driver
            self.logger.info("===== Starting Password change not allows same password Test =====")
            partner_profile_page= PartnerProfilePage(self.driver)


            # Test steps
            time.sleep(1)
            partner_profile_page.click_profile_tab()
            time.sleep(2)
            self.logger.info("Clicked Profile tab")
            time.sleep(2)
            partner_profile_page.type_old_password("helloo")
            time.sleep(2)
            partner_profile_page.type_new_password("helloo")
            time.sleep(2)
            partner_profile_page.click_change_password()
            time.sleep(2)
            act_error_message=partner_profile_page.get_error_message()
            expected_error = "Use Different Password"

            if act_error_message == expected_error:
                print("Password is not able to change")

            else:
                print("Password is changed")

            time.sleep(4)
