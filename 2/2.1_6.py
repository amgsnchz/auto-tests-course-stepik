from selenium import webdriver
import time

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

try:

    browser.get(link)

# Проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element_by_id('peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('value of people radio: ', people_checked)
    assert people_checked is not None, 'People radio is not selected by default'

# Проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element_by_id('robotsRule')
    robots_checked = robots_radio.get_attribute('checked')
    print('value of robots_radio: ', robots_checked)
    assert robots_checked is None

# Проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element_by_css_selector('.btn')
    button_disabled = button.get_attribute('disabled')
    print('value of button Submit: ', button_disabled)
    assert button_disabled is None

# Проверяем значение атрибута disabled у кнопки Submit после таймаута
    time.sleep(10)
    button_disabled = button.get_attribute('disabled')
    print('value of button Submit after 10sec: ', button_disabled)
    assert button_disabled is not None

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
