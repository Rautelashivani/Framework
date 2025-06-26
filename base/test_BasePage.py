import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_Base:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver, request):
        self.driver = driver

        # Setup
        self.logger.info("******* Setting Up Test *******")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)


        self.lp.clickLogin()

        # verification that login succeeded
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: "dashboard" in d.current_url.lower()
            )
        except:
            self.logger.error("Login failed!")
            pytest.fail("Login failed - cannot proceed with test")

        # Teardown
        def finalizer():
            try:
                self.logger.info("******* Tearing Down Test *******")
                self.lp.clickLogout()
                # Verify logout succeeded
                WebDriverWait(self.driver, 5).until(
                    lambda d: "login" in d.current_url.lower()
                )
            except Exception as e:
                self.logger.warning(f"Teardown warning: {str(e)}")

        request.addfinalizer(finalizer)