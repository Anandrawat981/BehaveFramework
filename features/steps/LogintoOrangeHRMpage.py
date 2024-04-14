from behave import *
from selenium.webdriver.common.by import By


@when('user on oranageHRM home page')
def oranageHRMpage(context):
    context.driver.implicitly_wait(10)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('enter username "{id1}" and password "{pwd}"')
def validIDandPass(context,id1,pwd):
    context.driver.implicitly_wait(20)
    context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(id1)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(pwd)



@when('click on Login button')
def clicklogin(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('User should able to verify dasboard page with login succesfully')
def verifyDasboard(context):
    try:
        dasboard1 = context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed()
    except:
        context.driver.close()
        assert False,"Test Failed"
    if dasboard1 == "Dashboard":
        assert True, "Test Passed"




