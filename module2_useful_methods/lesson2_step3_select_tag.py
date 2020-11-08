"""
The task: https://stepik.org/lesson/228249/step/3?unit=200781
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

tested_link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(tested_link)

    num1 = str(browser.find_element_by_id('num1').text)
    num2 = str(browser.find_element_by_id('num2').text)
    operation = str(browser.find_element_by_css_selector('h2 > .nowrap:nth-child(3)').text)
    result = eval(num1 + operation + num2)

    select_field = Select(browser.find_element_by_id('dropdown'))
    select_field.select_by_value(str(result))

    submit = browser.find_element_by_css_selector('button.btn')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
