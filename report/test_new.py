""" 文件名命名不要用空格、特殊字符等"""
import unittest
from Daily.report import Init


class BaiduTestYe(Init):
        def test_baidu_news(self):
            """首页业务:在百度首页点击百度新闻"""
            self.driver.find_element_by_link_text('新闻').click()
            self.driver.ge('http://www.baidu.com')

        def test_baidu_shouYe(self):
            """首页业务：测试百度的title是否正确"""
            self.assertEqual(self.driver.title, '百度一下，')
if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(BaiduTestYe)




