"""
The task: https://stepik.org/lesson/165493/step/7?unit=140087
"""

from selenium import webdriver
import time
from math import log as ln, sin

tested_link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(tested_link)

    treasure = browser.find_element_by_id("treasure")
    x = int(treasure.get_attribute("valuex"))
    result = ln(abs(12 * sin(x)))

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(str(result))

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
