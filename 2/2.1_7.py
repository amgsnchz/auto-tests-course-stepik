from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))
    browser.get('http://suninjuly.github.io/get_attribute.html')

    value_x = browser.find_element_by_id('treasure').get_attribute('valuex')

    field = browser.find_element_by_id('answer')
    y = calc(value_x)
    field.send_keys(y)

    for selector in ['#robotCheckbox', '#robotsRule', 'button.btn']:
        browser.find_element_by_css_selector(selector).click()

finally:
    time.sleep(5)
    browser.quit()
