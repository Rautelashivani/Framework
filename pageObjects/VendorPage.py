from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VendorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
    vendor_link = (By.XPATH, "//span[normalize-space()='Vendors']")
    search_button = (By.XPATH, "//span[normalize-space()='Search']")
    search_field = (By.XPATH, "//input[@placeholder='Search Vendors']")
    partner_vendor = (By.XPATH, "//p[@aria-label='Titoo']")
    empanelment_button = (By.XPATH, "(//button[normalize-space()='Invite for Empanelment'])[1]")
    message_field = (By.XPATH, "//textarea[1]")
    invite_button = (By.CSS_SELECTOR, "div[role='presentation'] button:nth-child(2)")
    act_result = (By.XPATH, "//p[@class='text-title font-bold mt-4']")


    def click_vendor_link(self):
        self.wait.until(EC.element_to_be_clickable(self.vendor_link)).click()

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()

    def enter_search_text(self, text):
        self.wait.until(EC.visibility_of_element_located(self.search_field)).send_keys(text)

    def click_partner_vendor(self):
        self.wait.until(EC.element_to_be_clickable(self.partner_vendor)).click()

    def click_empanelment_button(self):
        self.wait.until(EC.element_to_be_clickable(self.empanelment_button)).click()

    def enter_message(self, text):
        self.wait.until(EC.visibility_of_element_located(self.message_field)).send_keys(text)

    def click_invite_button(self):
        self.wait.until(EC.element_to_be_clickable(self.invite_button)).click()

    def get_actual_result(self):
        return self.wait.until(EC.visibility_of_element_located(self.act_result)).text