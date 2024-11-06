from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
        EMAIL_FIELD= (By.XPATH, '//*[@id="email-2"]')
        PASSWORD_FIELD = (By.XPATH, '//*[@id="field"]')
        #CONTINUE_BUTTON = (By.XPATH, '//*[@id="wf-form-Sign-up"]/a')
        CONTINUE_BUTTON = (By.CSS_SELECTOR, "a.login-button[wized='loginButton']")

        def login(self, email, password):
                self.find_element(*self.EMAIL_FIELD).send_keys(email)
                self.find_element(*self.PASSWORD_FIELD).send_keys(password)
                self.find_element(*self.CONTINUE_BUTTON).click()

