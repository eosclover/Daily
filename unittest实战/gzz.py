#!/usr/bin/env python
#-*-coding:utf-8-*-
# @Author   : clover
# @Time    : 2018/7/5 16:46

import  unittest
from selenium import webdriver
import time
import requests


class gzz(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://xxxxxm:804/jzgxgzz/#/login')
    def tearDown(self):
        self.driver.quit()


    def test_login(self):
        self.driver.find_element_by_xpath('//*[@id="pane-usernameLogin"]/form/div[1]/div/div/input').send_keys('xxxxx')
        self.driver.find_element_by_xpath('//*[@id="pane-usernameLogin"]/form/div[2]/div/div/input').send_keys('654321')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="pane-usernameLogin"]/form/button').click()
        self.assertEqual(self.driver.current_url,'http://uat.lifesea.com:804/jzgxgzz/#/login')

    def test_assi(self):
        header_dict={"Content-Type": "application/json",
                     'authorization':'token=76a07f128e99471591f9ca4c3d18d89d',
                     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
        url='http://192.168.188.61:8106/jzgxgzz/docAssistant/assistantList'
        req=requests.get(url=url,params=header_dict)
        print(req.url)
        print(req.text)
        # self.driver.find_element_by_xpath('//*[@id="leftsideBar"]/ul/div/li[2]/div').click()
        # self.driver.find_element_by_xpath('//*[@id="leftsideBar"]/ul/div/li[2]/ul/a/li/span').click()
        # self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/button/span').click()
        # self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[1]/div/div[1]/input').send_keys('wy')
        # self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/div/div[1]/input').send_keys('test_0606')
        # self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[3]/div/div[1]/input').send_keys('test0606')
        # self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/span/button[1]/span').click()
        #
if __name__=='__main__':
    unittest.main()
