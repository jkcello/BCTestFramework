# -*- coding: utf-8 -*-
#把测试样例写成框架形式
from selenium import webdriver
from BCTestFramework.POM.dayanghomepage import DayangHomePage
import unittest, time

class TestCase1(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Edge()
        cls.driver.implicitly_wait(30)
        cls.driver.get('http://www.dayang.com.cn')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()   


    def test_dayangsearch_test_case(self): 
        dypage = DayangHomePage(self.driver)
        dypage.type_search('IP播出')
        dypage.switch_window()
        results = self.driver.find_elements_by_class_name("itb-detail")
        self.assertEqual(8, len(results))
        dypage.take_screenshot()
        
if __name__ == "__main__":
    unittest.main()