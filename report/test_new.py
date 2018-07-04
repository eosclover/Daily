""" 文件名命名不要用空格、特殊字符等"""
import unittest
from Daily.report.Init import Init


class Baidu(Init):
    def test_001(self):
        # print('第一个测试用例')
        """验证：测试百度首页点击新闻后的跳转"""
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[3]').click()
        self.driver.get('https://www.baidu.com')

    def test_002(self):
        # print('第二个测试用例')、
        """验证“测试百度首页点击地图后的跳转"""
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[3]').click()
        self.driver.get('https://www.baidu.com')

if __name__ == '__main__':
     unittest.main(verbosity=0)





