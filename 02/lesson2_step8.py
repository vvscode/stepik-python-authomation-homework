from selenium import webdriver
from selenium.webdriver.common.by import By
import os 

link = "http://suninjuly.github.io/file_input.html"
first_name = 'Vasiliy'
last_name = 'Vanchuk'
email = 'vvsc0de@gmail.com'

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'input[name=firstname]').send_keys(first_name)
    browser.find_element(By.CSS_SELECTOR, 'input[name=lastname]').send_keys(last_name)
    browser.find_element(By.CSS_SELECTOR, 'input[name=email]').send_keys(email)
    browser.find_element(By.CSS_SELECTOR, 'input[name=file]').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    alert.accept()

    print('Alert text: {}'.format(alert_text))
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()