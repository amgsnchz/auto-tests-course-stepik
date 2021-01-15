import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    print('\nstart browser for test..')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    print('\nquit browser..')
    browser.quit()


urls = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('url', urls)
def test_guest_should_see_login_link(browser, url):
    link = '{}'.format(url)
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element_by_tag_name('textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission').click()
    feedback = browser.find_element_by_css_selector('.smart-hints__hint').text
    assert feedback == 'Correct!'
