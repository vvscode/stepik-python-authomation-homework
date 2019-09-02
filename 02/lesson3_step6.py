from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_window = browser.window_handles[0]
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    answer = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    alert.accept()

    print('Alert text: {}'.format(alert_text))
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()