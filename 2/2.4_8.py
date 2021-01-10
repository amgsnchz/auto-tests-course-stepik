from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from math import log, sin
import time

browser = webdriver.Chrome()

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element_by_id('book').click()

    y = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_css_selector('#solve').click()

finally:
    time.sleep(5)
    browser.quit()
