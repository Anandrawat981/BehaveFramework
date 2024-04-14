from behave import *
from selenium.webdriver.common.by import By


@then('User should able to verify Time at Work on dasboard page')
def step_impl(context):
    try:
        timework = context.driver.find_element(By.XPATH, "//p[text()='Time at Work']").text
    except:
        assert False,"Test Failed"
    if timework == "Time at Work":
        assert True,"Test Passed"
    context.driver.quit()


@then('User should able to verify My Actions on dasboard page')
def step_impl(context):
    try:
        myactions = context.driver.find_element(By.XPATH, "//p[text()='My Actions']").text
    except:
        assert False,"Test Failed"
    if myactions == "My Actions":
        assert True,"Test Passed"
    context.driver.quit()


