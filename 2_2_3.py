from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element_by_id("num1")
    second = browser.find_element_by_id("num2")
    first_n = int(first.text)
    second_n = int(second.text)
    sum = first_n + second_n
    sum_str = str(sum)
    list = browser.find_element_by_id("dropdown").click()
    n = browser.find_element_by_css_selector(f"[value = '{sum_str}']").click()
    input4 = browser.find_element_by_tag_name("button")
    input4.click()


finally:
    time.sleep(3)
    browser.quit()
