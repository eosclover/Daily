import unittest
import os
import HTMLTestRunner


def allTestCase():
    '''返回所有的测试用例'''
    suite = unittest.defaultTestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite

def run():
    '''生成测试报告'''
    fp = open('testReport.html', 'wb')
    HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='clover-UI自动化测试报告',
        description='基于Python语言的接口自动化测试实战').run(allTestCase())
run()