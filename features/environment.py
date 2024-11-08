from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application


def browser_init(context, browser ='firefox'):
    """
    :param context: Behave context
    """

    if browser == 'chrome':
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
        context.driver = webdriver.Chrome(service=service, options = chrome_options)

    elif browser == 'firefox':
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(driver_path)
        context.driver = webdriver.Firefox(service=service)


    context.app = Application(context.driver)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
