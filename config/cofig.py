# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 12:14
# @Author  : HCH
from selenium import webdriver
# 1 代表chrome有界面 2代表无界面
chrome_zt = 1


def IsOpenBrower(self):
    if chrome_zt == 1:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    elif chrome_zt == 2:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # selenium_chrome_driver_path = ""    # chromedriver 存放的路径
        self.driver = webdriver.Chrome(chrome_options=options)   # 可添加path参数
    return self.driver


# 账号密码
user = '15911061917'
pwd = 'zh@123456'
# cjd
userInfo = {
    'user': '15911061917',
    'pwd': 'zh@123456'
}
