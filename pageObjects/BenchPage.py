from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BenchPage:
        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

        # Locators
        bench_tab = (By.XPATH, "(//span[normalize-space()='Bench'])[1]")
        tech_stack_button = (By.XPATH, "//button[normalize-space()='Tech Stack']")
        stack_search_field = (By.XPATH, "//input[@placeholder='Search Resources']")
        jira_result = (By.XPATH, "//th[normalize-space()='JIRA']")
        matching_positions = (By.XPATH, "//tbody/tr[1]/th[2]/div[1]/div[1]/div[1]/div[2]")
        matching_search = (By.XPATH, "//input[@placeholder=\"Search\"]")
        matching_result = (By.XPATH, "(//div[normalize-space()='Java Developer'])[1]")
        cancel_button = (By.CSS_SELECTOR, "div[class='px-8 flex'] svg")

        # Page methods
        def click_bench_tab(self):
            self.wait.until(EC.element_to_be_clickable(self.bench_tab)).click()

        def click_tech_stack(self):
            self.wait.until(EC.element_to_be_clickable(self.tech_stack_button)).click()

        def search_tech_stack(self, text):
            self.wait.until(EC.visibility_of_element_located(self.stack_search_field)).send_keys(text)

        def get_jira_result_text(self):
            return self.wait.until(EC.visibility_of_element_located(self.jira_result)).text

        def click_matching_positions(self):
            self.wait.until(EC.element_to_be_clickable(self.matching_positions)).click()

        def type_matching_search(self, text):
            self.wait.until(EC.visibility_of_element_located(self.matching_search)).send_keys(text)

        def get_matching_result(self):
            return self.wait.until(EC.visibility_of_element_located(self.matching_result)).text

        def click_cancel_button(self):
            self.wait.until(EC.element_to_be_clickable(self.cancel_button)).click()