# 登录
# codeing=utf-8
import os
import unittest

from selenium import webdriver
import time
# import unittest
# from HTMLTestRunner import HTMLTestRunner
# from framework.base_page import BasePage
from config.cofig import *
# 用户名：15911061912 密码：zh@123456


class Login(unittest.TestCase):


    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        test_d = os.path.dirname(os.path.dirname(__file__))  # 当前脚本所在的大文件夹
        img_p = os.path.join(test_d, 'img')  # 测试用例文件夹
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_p), img_name))


    def setUp(self):
        if chrome_zt == 1:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        elif chrome_zt == 2:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            # selenium_chrome_driver_path = ""    #chromedriver 存放的路径
            self.driver = webdriver.Chrome(chrome_options=options)  # 可添加path参数



    def login(self,username,password):
        self.driver.get('https://manage.joinshare.newssdk.com/login')
        self.login_suc_url = 'https://manage.joinshare.newssdk.com/ent/index?id=67'
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[3]/span[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[2]/input').send_keys(password)
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/a').click()





