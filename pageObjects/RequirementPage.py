from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class RequirementPage:
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

        # Locators
        requirement_tab = (By.XPATH, "//span[normalize-space()='Requirements']")
        matching_positions = (By.XPATH, "//tbody/tr[1]/th[2]/div[1]/div[2]/div[2]")
        search_resources = (By.XPATH, "//input[@placeholder=\"Search Resources\"]")
        search_result = (By.XPATH, "(//div[@class='cursor-pointer hover:text-indigo-700'])[1]")
        can_cel= (By.XPATH, "(//*[name()='svg'][@class='absolute cursor-pointer left-[8px] top-[11px]'])[1]")


        # Page methods
        def click_requirement_tab(self):
            self.wait.until(EC.element_to_be_clickable(self.requirement_tab)).click()

        def click_matching_positions(self):
            self.wait.until(EC.element_to_be_clickable(self.matching_positions)).click()

        def type_search_resources(self, text):
            self.wait.until(EC.visibility_of_element_located(self.search_resources)).send_keys(text)

        def get_search_result(self):
            return self.wait.until(EC.visibility_of_element_located(self.search_result)).text

        def click_cancel(self):
            self.wait.until(EC.element_to_be_clickable(self.can_cel)).click()