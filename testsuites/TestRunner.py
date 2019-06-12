# coding=utf-8
from BCTestFramework.engine import HTMLTestRunnerMine
import os
import unittest
import time
from BCTestFramework.testsuites.testcase1 import TestCase1 
from BCTestFramework.testsuites.testcase2 import TestCase2
from BCTestFramework import testsuites as testsuites


 
# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
 
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLReport.html"
fp = open(HtmlFile, "wb")

# 构建suite
# suite = unittest.TestLoader().discover("testsuites")

search_tests = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
in_tests = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
suite = unittest.TestSuite([search_tests,in_tests])

 
if __name__ =='__main__':
 
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunnerMine.HTMLTestRunner(stream=fp, title=u"大洋官网测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)