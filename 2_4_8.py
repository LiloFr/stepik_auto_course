import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    btn = browser.find_element_by_id("book").click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    input4 = browser.find_element_by_id("solve")
    input4.click()

finally:
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(': ')[-1])

    # закрываем браузер после всех манипуляций
    browser.quit()