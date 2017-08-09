#!/usr/bin/python
# coding=utf-8
import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '4.4',
                        'deviceName': '192.168.56.101:5555',
                        'appPackage': 'com.android.calculator2',
                        'appActivity': '.Calculator',
                        'unicodeKeyboard': 'True',
                        'resetKeyboard': 'True'}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testAdd(self):
        number8 = self.driver.find_element_by_id('digit8')
        number8.click()

        addOperator = self.driver.find_element_by_id('plus')
        addOperator.click()

        number5 = self.driver.find_element_by_id('digit5')
        number5.click()

        equalOperator = self.driver.find_element_by_id('equal')
        equalOperator.click()

        try:
            value = self.driver.find_element_by_class_name('android.widget.EditText').text
            self.assertEqual(u'13', value)
        except Exception:
            print u"程序出现问题了"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
