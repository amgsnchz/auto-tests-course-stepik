from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    browser.get('http://suninjuly.github.io/alert_accept.html')

    browser.find_element_by_css_selector('.btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    y = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(5)
    browser.quit()
