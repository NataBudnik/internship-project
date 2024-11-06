from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class ContactUsPage(Page):
    CONTACT_US = (By.XPATH, "//div[@class='setting-text' and text()='Contact us']")
    SOCIAL_MEDIA_ICONS = (By.CSS_SELECTOR, 'a.contact-button.w-inline-block')
    CONNECT_COMPANY_BTN = (By.CSS_SELECTOR, 'a.button-link-menu._1')

    def click_contact_us(self):
        #self.click(self.CONTACT_US)
        self.wait.until(EC.element_to_be_clickable(self.CONTACT_US)).click()


    def verify_social_media_icons(self):
        icons = self.find_elements(*self.SOCIAL_MEDIA_ICONS)
        return len(icons) >=4

    def verify_connect_company_btn(self):
        return self.is_clickable(*self.CONNECT_COMPANY_BTN)