from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_name="email"
    textbox_password_name="password"
    button_login_css="button[type=\"submit\"]"
    path_logout_xpath="(//div[@class='text-info flex items-center justify-end text-indigo-500 cursor-pointer px-2 hover:text-indigo-700'])[1]"

    def __init__(self,driver):
        self.driver=driver

    def clearUserName(self,username):
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(Keys.DELETE)

    def clearPassword(self,password):
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(Keys.DELETE)

    def setUserName(self,username):

       self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)


    def setPassword(self, password):

       self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_css).click()


    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.path_logout_xpath).click()
