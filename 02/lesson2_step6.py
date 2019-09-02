from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    answer = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(str(answer))

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    button.click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    alert.accept()

    print('Alert text: {}'.format(alert_text))
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()