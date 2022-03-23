from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 150);")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    input2 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    input2.click()
    input3 = browser.find_element_by_css_selector("[for='robotsRule']")
    input3.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()