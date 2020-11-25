"""
The task: https://stepik.org/lesson/184253/step/6?unit=158843
"""

from selenium import webdriver
import time
from math import log as ln, sin

tested_link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(tested_link)

    troll_btn = browser.find_element_by_css_selector('button.btn')
    troll_btn.click()

    first_tab = browser.window_handles[0]
    second_tab = browser.window_handles[1]

    browser.switch_to.window(second_tab)

    x_value = browser.find_element_by_id('input_value')
    result = ln(abs(12*sin(int(x_value.text))))

    answer_input = browser.find_element_by_id('answer')
    answer_input.send_keys(str(result))

    submit_btn = browser.find_element_by_css_selector('button.btn')
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()
