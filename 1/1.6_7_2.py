from selenium import webdriver
import time
import random
import string

letters = string.ascii_lowercase
browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/huge_form.html')
    elements = browser.find_elements_by_css_selector('input[type="text"]')
    for element in elements:
        random_word = ''.join(random.choice(letters) for _ in range(8))
        element.send_keys(random_word)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
