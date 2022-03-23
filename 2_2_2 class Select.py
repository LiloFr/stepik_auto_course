from selenium import webdriver
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python