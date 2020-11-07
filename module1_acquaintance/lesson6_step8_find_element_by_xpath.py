"""
The task: https://stepik.org/lesson/138920/step/8?unit=196194
"""

from selenium import webdriver
import time


link_tested_site = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link_tested_site)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    searched_button = browser.find_element_by_xpath("//button[text()='Submit']")
    searched_button.click()
finally:
    time.sleep(15)
    browser.quit()
