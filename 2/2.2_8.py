from selenium import webdriver
import os
import time

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/file_input.html')
    for inp in browser.find_elements_by_css_selector('.form-group input'):
        inp.send_keys('data')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'test_doc.txt'
    file_path = os.path.join(current_dir, file_name)
    browser.find_element_by_id('file').send_keys(file_path)

    browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(5)
    browser.quit()
