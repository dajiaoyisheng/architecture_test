#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 14:22
# @Author  : HCH
from BeautifulReport import BeautifulReport
from selenium.webdriver.support.wait import WebDriverWait
from framework.login import Login
from selenium import webdriver
import unittest
import time
from config.cofig import *


"""
joinshare 首页测试
"""

class Index(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.index_url = 'https://manage.joinshare.newssdk.com/ent/index?id=68'
        if chrome_zt==1:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        elif chrome_zt==2:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            # selenium_chrome_driver_path = ""    #chromedriver 存放的路径
            self.driver = webdriver.Chrome(chrome_options=options)   #可添加path参数



    @BeautifulReport.add_test_img('test_Jump_1_pyq')
    def test_Jump_1_pyq(self):
        """朋友圈跳转"""
        Login.login(self, user, pwd)
        self.driver.get(self.index_url)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[2]/section/div[1]/p').click()
        # Jump_pyq_now_url = self.driver.current_url
        Jump_pyq_text=self.driver.find_element_by_class_name('template-item').text
        self.assertEqual(Jump_pyq_text, '新建空白海报')
        Login.save_img(self,'test_Jump_1_pyq')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_Jump_2_wz')
    def test_Jump_2_wz(self):
        """文章跳转"""
        self.driver.get(self.index_url)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[2]/section/div[2]/p').click()
        Jump_wz_text = self.driver.find_element_by_class_name('template-item').text
        self.assertEqual(Jump_wz_text, '新建文章')
        Login.save_img(self,'test_Jump_2_wz')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_Jump_3_hdH5')
    def test_Jump_3_hdH5(self):
        """互动H5跳转"""
        self.driver.get(self.index_url)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[2]/section/div[3]/p').click()
        Jump_hdH5_now_url = self.driver.current_url
        self.assertEqual(Jump_hdH5_now_url, 'https://manage.joinshare.newssdk.com/act/templatelist?tem=6')
        Login.save_img(self,'test_Jump_3_hdH5')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_Jump_4_wbH5')
    def test_Jump_4_wbH5(self):
        """外部h5跳转"""
        self.driver.get(self.index_url)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[2]/section/div[4]/p').click()
        Jump_wbH5_text = self.driver.find_element_by_class_name('template-item').text
        self.assertEqual(Jump_wbH5_text, '新建外部H5链接')
        Login.save_img(self,'test_Jump_4_wbH5')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_Jump_5_qcjdyr')
    def test_Jump_5_qcjdyr(self):
        """创建代言人跳转"""
        self.driver.get(self.index_url)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[1]/div[2]/div[1]/p[2]/a').click()
        Jump_5_qcjdyr_now_url = self.driver.current_url
        self.assertEqual(Jump_5_qcjdyr_now_url, 'https://manage.joinshare.newssdk.com/dept/add')
        Login.save_img(self,'test_Jump_5_qcjdyr')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_Jump_6_qcjhd')
    def test_Jump_6_qcjhd(self):
        """创建互动跳转"""
        self.driver.get(self.index_url)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[1]/div[2]/div[2]/p[2]/a').click()
        Jump_6_qcjhd_now_url = self.driver.current_url
        self.assertEqual(Jump_6_qcjhd_now_url, 'https://manage.joinshare.newssdk.com/act/templatelist')
        Login.save_img(self, 'test_Jump_6_qcjhd')
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()