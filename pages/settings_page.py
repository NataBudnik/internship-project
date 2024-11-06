from selenium.webdriver.common.by import By
from pages.base_page import Page


class SettingsPage(Page):
    SETTINGS_MENU = (By.XPATH , "//div[@class='menu-button-text' and text()='Settings']")
    CONTACT_US_OPTIONS = (By.ID , "contact_us_options")

    def click_settings(self):
        self.click(*self.SETTINGS_MENU)

    def click_contact_us_options(self):
        self.click(*self.CONTACT_US_OPTIONS)