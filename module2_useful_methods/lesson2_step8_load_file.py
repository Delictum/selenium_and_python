"""
The task: https://stepik.org/lesson/228249/step/8?unit=200781
"""

from selenium import webdriver
import time
import os


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "lesson2_step8_load_file.txt")

tested_link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(tested_link)

    input_fields = browser.find_elements_by_css_selector(".form-group input")
    for input_field in input_fields:
        input_field.send_keys(input_field.get_attribute("name"))

    file_input = browser.find_element_by_css_selector("input[type='file']")
    file_input.send_keys(file_path)

    submit_btn = browser.find_element_by_css_selector("button.btn")
    submit_btn.click()

finally:
    time.sleep(5)
    browser.quit()
