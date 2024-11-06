from behave import given, when, then
from time import sleep

@given ('open the main page')
def open_main(context):
    context.app.main_page.open_main_page()
    sleep(7)

@when('log in to the page')
def log_in(context):
    context.app.login_page.login("natabudnik.w@gmail.com","Bober88")


@when('click on setting option')
def click_settings(context):
    context.app.settings_page.click_settings()

@when('click on Contact us option')
def click_contact_us(context):
    context.app.contactUs_page.click_contact_us()

@then('verify the right page opens')
def verify_right_page(context):
    assert context.driver.current_url == "https://soft.reelly.io/contact-us"

@then('verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    assert context.app.contactUs_page.verify_social_media_icons()

@then ('verify "Connect the company" button is available and clickable')
def verify_connect_company_btn(context):
    assert context.app.contactUs_page.verify_connect_company_btn()





