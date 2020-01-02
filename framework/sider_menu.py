# 登录
# codeing=utf-8
from selenium import webdriver
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

class Login(object):

    def newevent_page(self):
        # 等待loading消失后点击做活动下拉框
        self.my_find_ele_load('xpath', '//*[@id="app"]/aside/div/div[2]/div/div[2]/p').click()
        # 点击下拉菜单中的新建活动进入新建活动页面
        self.driver.find_element_by_xpath('//*[@id="app"]/aside/div/div[2]/div/div[2]/ul/li[1]').click()
        # 等待loading消失后点击新建活动模板
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[2]/div[1]').click()

if __name__ == '__main__':
    # unittest.main()
    login = Login(webdriver.Firefox())
    # login.openBrower()
    login.handler_login()
