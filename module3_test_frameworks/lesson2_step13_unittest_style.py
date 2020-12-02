"""
The task: https://stepik.org/lesson/36285/step/13?unit=162401
"""

import time
import unittest
from selenium import webdriver


class TestRegister(unittest.TestCase):
    def test_register1(self):
        link_tested_site = "http://suninjuly.github.io/registration1.html"
        try:
            browser = webdriver.Chrome()
            browser.get(link_tested_site)

            input_first_name = browser.find_element_by_css_selector(".first_class > input[required='']")
            input_first_name.send_keys("Ihar")
            time.sleep(0.3)

            input_email = browser.find_element_by_css_selector(".second_class > input[required='']")
            input_email.send_keys("Alishkevich")
            time.sleep(0.3)

            input_email = browser.find_element_by_css_selector(".third_class > input[required='']")
            input_email.send_keys("IharAlishkevich@gmail.com")
            time.sleep(0.3)

            submit_button = browser.find_element_by_css_selector("button.btn")
            submit_button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration1 failed")

        finally:
            time.sleep(1)
            browser.quit()

    def test_register2(self):
        link_tested_site = "http://suninjuly.github.io/registration2.html"
        try:
            browser = webdriver.Chrome()
            browser.get(link_tested_site)

            input_first_name = browser.find_element_by_css_selector(".first_class > input[required='']")
            input_first_name.send_keys("Ihar")
            time.sleep(0.3)

            input_email = browser.find_element_by_css_selector(".second_class > input[required='']")
            input_email.send_keys("Alishkevich")
            time.sleep(0.3)

            input_email = browser.find_element_by_css_selector(".third_class > input[required='']")
            input_email.send_keys("IharAlishkevich@gmail.com")
            time.sleep(0.3)

            submit_button = browser.find_element_by_css_selector("button.btn")
            submit_button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration2 failed")

        finally:
            time.sleep(1)
            browser.quit()


if __name__ == '__main__':
    unittest.main()
