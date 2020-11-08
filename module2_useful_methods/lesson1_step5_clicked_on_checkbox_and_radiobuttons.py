"""
The task: https://stepik.org/lesson/165493/step/5?unit=140087
"""

from selenium import webdriver
import time
from math import log as ln, sin


tested_link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(tested_link)

    x = int(browser.find_element_by_id("input_value").text)
    result = ln(abs(12 * sin(x)))

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(str(result))

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
