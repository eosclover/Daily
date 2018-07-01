import unittest
from selenium import webdriver


class Init(unittest.TestCase):
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.baidu.com/')
        # driver.find_element_by_id('kw').send_keys('selenium')
        # driver.find_element_by_id('su').click()
        # time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        # driver.close()
# 调用函数
# Init()





