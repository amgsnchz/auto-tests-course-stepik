import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser for test..')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nquit browser..')
    browser.quit()


languages = [
    ('ru', 'русский'),
    ('de', 'немецкий'),
    pytest.param('ua', 'украинский', marks=pytest.mark.xfail(reason='no ua language')),
    ('en-gb', 'английский')
]


@pytest.mark.parametrize('code, lang', languages)
def test_guest_should_see_login_link(browser, code, lang):
    link = 'http://selenium1py.pythonanywhere.com/{}/'.format(code)
    print('Проверяемый язык %s' % lang)
    browser.get(link)
    browser.find_element_by_css_selector('#login_link')
