"""
The task: https://stepik.org/lesson/181384/step/8?unit=156009
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from math import log as ln, sin
import time

tested_link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(tested_link)

    price_h5 = WebDriverWait(browser, 13).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    book_btn = browser.find_element_by_id('book')
    book_btn.click()

    input_value = browser.find_element_by_id('input_value')
    x = int(input_value.text)
    result = ln(abs(12 * sin(x)))

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(str(result))

    time.sleep(30)
finally:
    time.sleep(5)
    browser.quit()
