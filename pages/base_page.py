from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, *locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self,*locator):
        element = self.find_element(*locator)
        element.click()

    def is_clickable(self, *locator):
        element = self.find_element(*locator)
        return element.is_displayed()