"""
The task: https://stepik.org/lesson/138920/step/7?unit=196194
"""

from selenium import webdriver
import time


link_tested_site = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link_tested_site)

    input_elements = browser.find_elements_by_tag_name("input")
    for input_element in input_elements:
        input_element.send_keys("Answer")

    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()
finally:
    time.sleep(15)
    browser.quit()
