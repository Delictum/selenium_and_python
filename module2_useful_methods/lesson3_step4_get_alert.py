"""
The task: https://stepik.org/lesson/184253/step/4?unit=158843
"""

from selenium import webdriver
import time
from math import log as ln, sin


tested_link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(tested_link)

    submit_btn = browser.find_element_by_css_selector('button.btn')
    submit_btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    input_value_x = browser.find_element_by_id('input_value')
    x = int(input_value_x.text)
    result = ln(abs(12 * sin(x)))

    answer_input = browser.find_element_by_id('answer')
    answer_input.send_keys(str(result))

    submit_btn = browser.find_element_by_css_selector('button.btn')
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
