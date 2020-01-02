from selenium import webdriver
import time
import os
from BeautifulReport import BeautifulReport
import unittest
import re
import inspect
from config.cofig import *


# from indexcase import Lindex
# 用户名：15911061912 密码：zh@123456
# 密码错误
# 账号不是手机号
# 账号不存在
# 账号密码正确，登录到首页

class LoginTest(unittest.TestCase):

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
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
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



    def login(self, username, password):
        self.driver.get('https://manage.joinshare.newssdk.com/login')
        self.login_suc_url = 'https://manage.joinshare.newssdk.com/ent/index?id=67'
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div[3]/span[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[1]/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/div[2]/input').send_keys(password)
        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[1]/a').click()

    # @unittest.skip
    @BeautifulReport.add_test_img('test_login1')
    def test_login1(self):
        """账号密码正确"""
        self.login(user, pwd)
        time.sleep(2)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[2]/h4').text
        self.save_img("test_login1")
        self.assertTrue(message,'我要营销')


    # @unittest.skip
    @BeautifulReport.add_test_img('test_login2')
    def test_login2(self):
        '''账号正确,密码错误'''
        self.login('15911061912', '000000')
        self.driver.implicitly_wait(2)
        error_message = self.driver.find_element_by_xpath('//*[contains(@id,"layui-layer")]/div').text
        self.save_img("test_login2")
        self.assertEqual(error_message,'你填写的账号或密码不正确')


    # @unittest.skip
    @BeautifulReport.add_test_img('test_login3')
    def test_login3(self):
        '''账号错误,密码正确'''
        self.login('123456789', pwd)
        self.driver.implicitly_wait(2)
        error_message = self.driver.find_element_by_xpath('//*[contains(@id,"layui-layer")]/div').text
        self.save_img("test_login3")
        self.assertEqual(error_message,'你填写的账号或密码不正确' )


    # @unittest.skip
    @BeautifulReport.add_test_img('test_login4')
    def test_login4(self):
        '''用户名为空'''
        self.login('', 'zh@123456')
        self.driver.implicitly_wait(2)
        error_message = self.driver.find_element_by_xpath('//*[contains(@id,"layui-layer")]/div').text
        self.save_img("test_login4")
        self.assertEqual(error_message,'请填写管理员账号')

    # @unittest.skip
    @BeautifulReport.add_test_img('test_login5')
    def test_login5(self):
        '''密码为空'''
        self.login('15911061912', '')
        self.driver.implicitly_wait(2)
        error_message = self.driver.find_element_by_xpath('//*[contains(@id,"layui-layer")]/div').text
        self.save_img("test_login5")
        self.assertEqual(error_message, '你填写的账号或密码不正确' )

    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()


