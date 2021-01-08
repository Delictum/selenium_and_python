"""
The task: https://stepik.org/lesson/237240/step/9?unit=209628
"""

import time

from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def is_element_exist_by_class_name(browser, selector: str) -> bool:
    """
    Checks for an element by class name.

    :param browser: Selenium browser instance
    :param selector: class name
    :return: True if element exists else False
    """
    try:
        browser.find_element_by_class_name(selector)
        return True
    except NoSuchElementException:
        return False


def test_exist_add_to_basket_btn(browser):
    """
    The test verifies that the product page on the site contains an add to cart button.
    """

    browser.get(link)
    time.sleep(30)
    assert is_element_exist_by_class_name(browser, "btn-add-to-basket"), "Element doesn't exist"


# def test_exist_basket(browser):
#     """
#     The test confirms that there is a shopping cart element on the product page on the site.
#     """
#
#     browser.get(link)
#     time.sleep(3)
#     assert is_element_exist_by_class_name(browser, "basket"), "Element doesn't exist"
