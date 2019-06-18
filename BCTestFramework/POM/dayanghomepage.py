#大洋首页页面对象
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from BCTestFramework.engine.logger import Logger

logger = Logger(logger="DayangHomePage").getlog()

class DayangHomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.btn = driver.find_element_by_id("btnChange")
        self.searchbox = driver.find_element_by_name("search_text")

    def type_search(self,text):
        self.btn.click()
        self.searchbox.clear()       
        self.searchbox.send_keys(text)
        self.searchbox.send_keys(Keys.ENTER)  
        logger.info("Had search \' %s \' in inputBox" % text)

    def take_screenshot(self):
        file_path = os.path.dirname(os.getcwd()) + '\\Screenshots\\'
        rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try :
            #self.driver.get_screenshot_as_file("C:\\python36\\mypy\\selenium\\test\\Screenshots\\test1.png")        
            self.driver.get_screenshot_as_file(screen_name)
        except Exception as e:
        	print('error')

    def switch_window(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.close()
                self.driver.switch_to.window(handle)
     

# file_path = os.path.dirname(os.getcwd()) + '\\Screenshots\\'
# rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
# screen_name = file_path + rq + '.png'
# print(screen_name)
