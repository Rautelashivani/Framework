
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class MemberPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    member_tab = (By.XPATH, "//span[normalize-space()='Members']")
    name_element = (By.XPATH, "(//div[@class='flex justify-between'])[1]")
    delete_icon = (By.XPATH,"(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-colorError MuiSvgIcon-fontSizeSmall css-qrs4ze'])[1]")
    delete_button = (By.XPATH, "(//button[normalize-space()='Delete'])[1]")


    def click_member_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.member_tab)).click()

    def get_name_element(self):
        return self.wait.until(EC.element_to_be_clickable(self.name_element))

    def get_delete_icon(self):
        return self.wait.until(EC.element_to_be_clickable(self.delete_icon))


    def delete_member(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_name_element()).click().perform()
        time.sleep(1)
        actions.move_to_element(self.get_delete_icon()).click().perform()

    def click_delete_button(self):
        self.wait.until(EC.element_to_be_clickable(self.delete_button)).click()


