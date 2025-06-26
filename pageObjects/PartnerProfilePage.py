from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PartnerProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
    profile_tab = (By.XPATH, "//p[@class='text-info truncate text-ellipsis']")
    old_password = (By.XPATH, "//input[@name=\"oldPassword\"]")
    new_password = (By.XPATH, "//input[@name=\"newPassword\"]")
    change_password = (By.XPATH, "(//button[normalize-space()='Change Password'])[1]")
    error_message = (By.XPATH, "//p[text()='Use Different Password']")


        # Page methods
    def click_profile_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_tab)).click()

    def type_old_password(self, text):
        self.wait.until(EC.visibility_of_element_located(self.old_password)).send_keys(text)

    def type_new_password(self, text):
        self.wait.until(EC.visibility_of_element_located(self.new_password)).send_keys(text)

    def click_change_password(self):
        self.wait.until(EC.element_to_be_clickable(self.change_password)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text

