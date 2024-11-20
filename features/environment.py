from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    bs_user = 'natalyabudnik_V873Ue'
    bs_key = 'sfN3tr1b9bSiMszydpcJ'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'



    options = Options()
    bstack_options = {
      #  "os" : "Windows",
       # "osVersion" : "11",
       # 'browserName': 'chrome',
       # 'sessionName': scenario_name,
   # }
   # options.set_capability('bstack:options', bstack_options)
   # context.driver = webdriver.Remote(command_executor=url, options=options)

      "deviceName" : "iPhone 15 Pro",
        "osVersion" : "18",
        'browserName': 'safari',
        'sessionName': scenario_name,
    }

    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)





   # context.driver.maximize_window()
   # context.driver.implicitly_wait(4)
    #context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()








