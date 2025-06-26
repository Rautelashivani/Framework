
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.out_position = (By.XPATH,"//h5[@class='MuiTypography-root MuiTypography-h5 !text-indigo-950 css-1faowcc']")
        self.table_rows = (By.XPATH, "//table//tbody//tr")

    def get_header_value(self):
        header_element = self.wait.until(EC.presence_of_element_located(self.out_position))
        return int(header_element.text.strip())

    def click_header(self):
        header_element = self.wait.until(EC.element_to_be_clickable(self.out_position))
        header_element.click()

    def sum_numbers_before_parentheses(self):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.table_rows))
        total_sum = 0

        for row in rows:
            try:
                cell = row.find_element(By.XPATH, ".//td[3]")
                cell_text = cell.text.strip()

                # Extract number before parentheses
                number_str = cell_text.split("(")[0].strip()
                number = int(number_str)

                total_sum += number
                print(f"Found value: {number}")

            except Exception as e:
                print(f"Couldn't parse value in row: {str(e)}")

        print(f"Total sum: {total_sum}")
        return total_sum