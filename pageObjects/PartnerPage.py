from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class PartnerPage:
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

        # Locators
        partner_tab = (By.XPATH, "//span[normalize-space()='Partners']")
        empaneled_tab = (By.XPATH, "//span[normalize-space()='Empaneled']")
        search_partner = (By.XPATH, "//input[@placeholder=\"Search Partners\"]")
        search_result = (By.XPATH, "//p[@aria-label='IBM']")


        # Page methods
        def click_partner_tab(self):
            self.wait.until(EC.element_to_be_clickable(self.partner_tab)).click()

        def click_empaneled_tab(self):
            self.wait.until(EC.element_to_be_clickable(self.empaneled_tab)).click()

        def type_search_partner(self, text):
            self.wait.until(EC.visibility_of_element_located(self.search_partner)).send_keys(text)

        def get_search_result(self):
            return self.wait.until(EC.visibility_of_element_located(self.search_result)).text