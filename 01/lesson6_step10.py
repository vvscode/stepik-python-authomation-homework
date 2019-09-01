from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time 

success_link = "http://suninjuly.github.io/registration1.html"
fail_link = "http://suninjuly.github.io/registration2.html"

required_fields_xpaths = [
    '//label[contains(text(), "First name")]/following-sibling::input',
    '//label[contains(text(), "Last name")]/following-sibling::input',
    '//label[contains(text(), "Email")]/following-sibling::input',
];

def run_test_on_page(browser, link):
    browser.get(link)

    for xpath in required_fields_xpaths:
        field = browser.find_element(By.XPATH, xpath)
        field.send_keys('Some value')

    time.sleep(1)

    submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    submit_button.click()

try:
    browser = webdriver.Chrome()

    number_of_passed_tests = 0

    print("Run test on correct page")
    run_test_on_page(browser, success_link)
    number_of_passed_tests = number_of_passed_tests + 1

    assert number_of_passed_tests == 1, "It should pass tests on correct page"

    try:
        print("Run test on incorrect page")
        run_test_on_page(browser, fail_link)
        assert False, "It should NOT pass tests on incorrect page"

    except NoSuchElementException as exception:
        print('Handled NoSuchElementException:')
        print(exception)
        number_of_passed_tests = number_of_passed_tests + 1

    assert number_of_passed_tests == 2, "It should get 2 expected results on the runs"

    print("Tests are passed")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()