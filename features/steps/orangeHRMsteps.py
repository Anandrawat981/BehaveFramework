from behave import *
from time import sleep
from selenium import webdriver
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@given('launch the chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@when('open orangeHRM home page')
def openHomepage(context):
    context.driver.implicitly_wait(20)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that logo present on the home page')
def verifyLogo(context):
    context.driver.implicitly_wait(10)
    status = context.driver.find_element(By.XPATH,"//div[@class='orangehrm-login-logo']").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.quit()

