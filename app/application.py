from pages.base_page import Page
from pages.main_page import MainPage
from pages.contactUs_page import ContactUsPage
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage

class Application:
    def __init__(self, driver):

        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.contactUs_page = ContactUsPage(driver)
        self.login_page = LoginPage(driver)
        self.settings_page = SettingsPage(driver)

