import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    def test_login_logout(self, driver):

         self.logger.info("******* Opening Browser *******")
         self.driver = driver
         self.driver.get(self.baseURL)

         self.lp = LoginPage(self.driver)

         self.lp.setUserName(self.username)

         self.lp.setPassword(self.password)

         self.lp.clickLogin()
         time.sleep(2)




         self.lp.clickLogout()