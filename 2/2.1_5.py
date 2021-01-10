from selenium import webdriver
import time
import math


def calc(xs):
    return str(math.log(abs(12*math.sin(int(xs)))))


browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    im_robot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    im_robot.click()

    robots_rule = browser.find_element_by_css_selector("[for='robotsRule']")
    robots_rule.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
