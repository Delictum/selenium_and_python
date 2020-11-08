"""
The task: https://stepik.org/lesson/228249/step/6?unit=200781
"""

from selenium import webdriver
import time
from math import log as ln, sin

tested_link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(tested_link)

    input_value_x = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_value_x)
    x = int(input_value_x.text)
    result = ln(abs(12 * sin(x)))

    answer_input = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true)", answer_input)
    answer_input.send_keys(str(result))

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true)", robot_checkbox)
    robot_checkbox.click()

    robots_rule = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true)", robots_rule)
    robots_rule.click()

    submit_btn = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true)", submit_btn)
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
