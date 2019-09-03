from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
acceptable_price = 100

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price_element = browser.find_element(By.ID, 'price')
    def is_price_acceptable(_):
      current_price = price_element.text.replace('$', '')
      print('Current price: {}'.format(current_price))
      return current_price and int(current_price) <= acceptable_price

    WebDriverWait(browser, 20).until(
        is_price_acceptable
    )

    print('Current price: {}$'.format(price_element.text.replace('$', '')))

    browser.find_element(By.CSS_SELECTOR, 'button#book').click()

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)

    answer = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(answer)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    alert.accept()

    print('Alert text: {}'.format(alert_text))
finally:
    # time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()