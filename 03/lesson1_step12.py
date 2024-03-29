import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

required_fields_xpaths = [
    '//label[contains(text(), "First name")]/following-sibling::input',
    '//label[contains(text(), "Last name")]/following-sibling::input',
    '//label[contains(text(), "Email")]/following-sibling::input',
]

success_link = "http://suninjuly.github.io/registration1.html"
fail_link = "http://suninjuly.github.io/registration2.html"

class TestRegistration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Setup class')
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        print('tear down class')
        TestRegistration.browser.quit()

    def abstract_registration(self, link):
        browser = TestRegistration.browser
        browser.get(link)

        for xpath in required_fields_xpaths:
            field = browser.find_element(By.XPATH, xpath)
            field.send_keys('Some value')

        time.sleep(1)

        submit_button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
        submit_button.click()
    
    def test_registration1(self):
        self.abstract_registration(success_link)
    
    def test_registration2(self):
        self.abstract_registration(fail_link)

if __name__ == "__main__":
    unittest.main()