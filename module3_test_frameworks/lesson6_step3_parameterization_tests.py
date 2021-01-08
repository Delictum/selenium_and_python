"""
The task: https://stepik.org/lesson/237240/step/3?unit=209628
"""

import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, url):
    browser.get(url)
    browser.implicitly_wait(3)
    area = browser.find_element_by_class_name("textarea")
    answer = math.log(int(time.time()))
    area.send_keys(str(answer))

    btn = browser.find_element_by_class_name("submit-submission")
    btn.click()

    hint = browser.find_element_by_class_name("smart-hints__hint")
    print(hint.text)
