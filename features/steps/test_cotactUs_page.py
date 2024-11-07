from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given ('open the main page')
def open_main(context):
    context.app.main_page.open_main_page()
    sleep(8)


@when('log in to the page')
def log_in(context):
    context.app.login_page.login("natabudnik.w@gmail.com","Bober88")
    sleep(8)


@when('click on setting option')
def click_settings(context):
    context.app.settings_page.click_settings()
    sleep(8)

@when('click on Contact us option')
def click_contact_us(context):
    context.app.contactUs_page.click_contact_us()
    sleep(8)

@then('verify the right page opens')
def verify_right_page(context):

    #WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]')))
    WebDriverWait(context.driver, 30).until(EC.url_contains("contact-us"))

    current_url = context.driver.current_url
    print(f"Current URL: {current_url}")
    #assert current_url == "https://soft.reelly.io/contact-us"
    assert "contact-us" in current_url




@then('verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    assert context.app.contactUs_page.verify_social_media_icons()

@then ('verify "Connect the company" button is available and clickable')
def verify_connect_company_btn(context):
    assert context.app.contactUs_page.verify_connect_company_btn()





