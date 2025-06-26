import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_MFLNL:
    baseURL = ReadConfig.getApplicationURL()
    wrongusername = ReadConfig.getWronguseremail()
    wrongpassword = ReadConfig.getWrongpassword()
    logger = LogGen.loggen()

    def test_multiple_failed_logins_no_lockout(self, driver):
        self.logger.info("******* Test_Base *******")
        self.driver = driver
        self.logger.info("===== Starting login with wrong credentials =====")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        # Run the test 5 times
        for attempt in range(1, 6):
            self.logger.info(f"===== Attempt {attempt} with wrong credentials =====")


                # Clear fields before each attempt (except first attempt)
            if attempt > 1:
                    self.lp.clearUserName(self.wrongusername)
                    self.lp.clearPassword(self.wrongpassword)
                    time.sleep(1)  # Small delay between attempts

                # Set credentials
            self.lp.setUserName(self.wrongusername)
            self.lp.setPassword(self.wrongpassword)
            self.lp.clickLogin()


            time.sleep(2)  # Wait to see the result

            self.logger.info(f"Attempt {attempt} completed")

