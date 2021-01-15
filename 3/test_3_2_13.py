from selenium import webdriver
import unittest


def link_place(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath('//div/div/input').send_keys('Alex')
    browser.find_element_by_xpath('//div/div[2]/input').send_keys('Alex')
    browser.find_element_by_xpath('//div/div[3]/input').send_keys('Alex')
    browser.find_element_by_css_selector('button.btn').click()

    return browser.find_element_by_tag_name('h1').text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_place('http://suninjuly.github.io/registration1.html'),
                         "Congratulations! You have successfully registered!",
                         "Ops, seems like result doesnt match your expectations")

    def test_reg2(self):
        self.assertEqual(link_place('http://suninjuly.github.io/registration2.html'),
                         "Congratulations! You have successfully registered!",
                         "Ops, seems like result doesnt match your expectations")


if __name__ == "__main__":
    unittest.main()
