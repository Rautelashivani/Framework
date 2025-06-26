from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SignupPage:
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

        # Locators
        sign_up = (By.XPATH, "(//span[@class='text-blue-500 cursor-pointer'])[1]")
        first_name = (By.XPATH, "//input[@name=\"firstName\"]")
        last_name = (By.XPATH, "//input[@name=\"lastName\"]")
        company_name = (By.XPATH, "//input[@name=\"companyName\"]")
        email_address = (By.XPATH, "//input[@name=\"email\"]")
        pass_word = (By.XPATH, "//input[@name=\"password\"]")
        conti_nue = (By.XPATH, "//button[@type=\"submit\"]")
        ale_rt = (By.XPATH, "(//p[@class='!mt-1 text-info text-red-500'])[1]")

        # Page methods
        def click_on_signup(self):
            self.wait.until(EC.element_to_be_clickable(self.sign_up)).click()

        def type_first_name(self,text):
            self.wait.until(EC.element_to_be_clickable(self.first_name)).send_keys(text)

        def type_last_name(self,text):
            self.wait.until(EC.element_to_be_clickable(self.last_name)).send_keys(text)

        def type_company_name(self, text):
            self.wait.until(EC.element_to_be_clickable(self.company_name)).send_keys(text)

        def type_email_address(self, text):
            self.wait.until(EC.element_to_be_clickable(self.email_address)).send_keys(text)

        def type_pass_word(self, text):
            self.wait.until(EC.element_to_be_clickable(self.pass_word)).send_keys(text)

        def click_on_continue(self):
            self.conti_nue.click()

        def get_alert(self):
            return self.wait.until(EC.visibility_of_element_located(self.ale_rt)).text
