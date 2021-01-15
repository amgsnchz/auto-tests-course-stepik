import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/ '


def test_button_is_presented_for_any_language(browser):
    browser.get(link)
    time.sleep(10)
    cart_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert cart_button is not None
