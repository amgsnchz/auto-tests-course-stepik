from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()

try:
    def calc(x):
        return str(log(abs(12 * sin(int(x)))))


    browser.get('http://suninjuly.github.io/execute_script.html')
    y = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id('answer').send_keys(y)
    im_robot = browser.find_element_by_css_selector('[for="robotCheckbox"]').click()
    button = browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    robots_rule = browser.find_element_by_css_selector('[for="robotsRule"]').click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()
