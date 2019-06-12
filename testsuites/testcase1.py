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
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.close()
                self.driver.switch_to.window(handle)
        results = self.driver.find_elements_by_class_name("itb-detail")
        dypage.take_screenshot()
        self.assertEqual(8, len(results))
        
        



if __name__ == "__main__":
    unittest.main()
