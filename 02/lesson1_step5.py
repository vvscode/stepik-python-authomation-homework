from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

    answer = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    alert.accept()

    print('Alert text: {}'.format(alert_text))
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()