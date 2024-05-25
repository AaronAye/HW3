from time import sleep

from behave import when, then
from selenium.webdriver.common.by import By


# @given('Open Target page')
#def open_target(context):
#    context.driver.get('https://www.target.com/')
 #   sleep(5)


@when('Click on sign in HW3')
def click_signin_icon(context):
    context.driver.find_element(By.XPATH, value="//span[contains(text(),'Sign in')]").click()

    # Click SignIn from side navigation
    context.driver.find_element(By.XPATH, value="//a[@data-test='accountNav-signIn']").click()
    sleep(5)

@then('Verify sign in message HW3')
def signin_text(context):
    actual_text = context.driver.find_element(By.XPATH, value="//span[contains(text(),'Sign into your Target account')]")

    # Assert
    assert 'Sign into your Target account' in actual_text.text, f'Error! Sign into your Target account not in {actual_text}'
    print("Test case has passed")

