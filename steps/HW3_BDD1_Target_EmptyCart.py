from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By

@when('Click on cart icon HW3')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, value="a[data-test='@web/CartLink']").click()
    sleep(5)

@then('Verify empty cart message HW3')
def verify_empty_cart_text(context):
     actual_text = context.driver.find_element(By.XPATH, value="//h1[text()='Your cart is empty']")
     assert 'Your cart is empty' in actual_text.text, f'Your cart is empty is not in {actual_text}'
     print("Test case has passed")



