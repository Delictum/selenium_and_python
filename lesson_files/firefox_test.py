from selenium import webdriver
import time

try:
    browser = webdriver.Firefox()

    browser.get("https://stepik.org/lesson/25969/step/12")
    time.sleep(5)

    textarea = browser.find_element_by_css_selector(".textarea")

    textarea.send_keys("get()")
    time.sleep(1)

    submit_button = browser.find_element_by_css_selector(".submit-submission")

    submit_button.click()
    time.sleep(5)
finally:
    browser.quit()
