from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/selects1.html')

    sum1 = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)

    Select(browser.find_element_by_css_selector('select')).select_by_value(str(sum1))

    browser.find_element_by_tag_name('.btn').click()

finally:
    time.sleep(5)
    browser.quit()
