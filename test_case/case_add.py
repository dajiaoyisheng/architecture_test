from BeautifulReport import BeautifulReport
import random
import re
import string
from selenium import webdriver
import unittest
import time
from framework.login import Login
from selenium.webdriver.common.by import By

from config.cofig import *


class Staff(unittest.TestCase):

    @classmethod
    def setUpClass(self):
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

        self.staff_num = []  # 添加前员工数
        self.staff_num2 = []  # 删除前员工数

    @BeautifulReport.add_test_img('test_add_1')
    def test_add_1(self):
        '''进入我的员工验证页面跳转'''
        Login.login(self, '15911061917', 'zh@123456')
        self.driver.find_element_by_xpath('//*[@id="app"]/aside/div/div[2]/div/div[4]/p').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/aside/div/div[2]/div/div[4]/ul/li[1]/a').click()
        self.driver.implicitly_wait(5)
        self.staff_url = 'https://manage.joinshare.newssdk.com/dept/index'
        message = self.driver.find_element_by_xpath('//*[@id="app"]/section/h1/span').text
        self.assertEqual(message, '代言人管理')  # 当前分组成员数
        time.sleep(3)
        sum_1 = self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section[1]/section/section[2]/h3').text  # 当前分组成员数
        self.number_sum_be = re.search(r'.*(\d+)', sum_1).group(1)
        self.staff_num.append(self.number_sum_be)
        Login.save_img(self, 'test_add_1')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_add_2')
    def test_add_2(self):
        '''新建成员页面是否跳转成功'''
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section[1]/section/section[2]/div[1]/div[2]/a[1]').click()  # 点击新建成员
        self.driver.implicitly_wait(5)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/section/h1/span').text
        self.assertEqual(message, '代言人管理 ／ 新建成员')
        Login.save_img(self, 'test_add_2')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_add_3')
    def test_add_3(self):
        '''填写信息'''
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[1]/div/input').send_keys(
            'black' + str(random.randint(1, 100)))
        seeds = string.digits
        random_str = random.choices(seeds, k=4)
        suiji = "".join(random_str)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[2]/div/input').send_keys(
            '17' + suiji + '54543')
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[3]/div/input').click()  # 点击所属分组
        self.driver.find_element_by_xpath('//*[@id="tree"]/div/ul/li/div/ul/li/div/div/span').click()  # 选择分组
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[6]/a[1]').click()  # 点击保存
        time.sleep(10)
        num = self.driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/section/section[2]/h3').text
        number_sum = re.search(r'.*(\d+)', num).group(1)  # 添加后员工数
        self.assertEqual(int(number_sum), int(self.staff_num[0]) + 1)
        Login.save_img(self, 'test_add_3')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_add_4')
    def test_add_4(self):
        '''[查看]按钮'''
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section[1]/section/section[2]/div[2]/table/tbody/tr[2]/td[9]/a[1]').click()
        self.driver.implicitly_wait(10)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/section/h1/span').text
        self.assertEqual(message, '代言人管理 ／ 查看成员')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[7]/a').click()
        Login.save_img(self, 'test_add_4')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_add_5')
    def test_add_5(self):
        '''[编辑]按钮'''
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section[1]/section/section[2]/div[2]/table/tbody/tr[2]/td[9]/a[2]').click()
        self.driver.implicitly_wait(10)
        message = self.driver.find_element_by_xpath('//*[@id="app"]/section/h1/span').text
        self.assertEqual(message, '代言人管理 ／ 编辑成员')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[6]/a[2]').click()
        Login.save_img(self, 'test_add_5')
        time.sleep(2)

    @BeautifulReport.add_test_img('test_add_6')
    def test_add_6(self):
        '''[删除]按钮'''
        time.sleep(3)
        num_1 = self.driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/section/section[2]/h3').text  # 删除前
        number_sum_1 = re.search(r'.*(\d+)', num_1).group(1)
        self.staff_num2.append(number_sum_1)  # 删除前
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/section/section[1]/section/section[2]/div[2]/table/tbody/tr[3]/td[9]/a[3]').click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        time.sleep(5)
        num = self.driver.find_element_by_xpath('//*[@id="app"]/section/section[1]/section/section[2]/h3').text
        number_sum_3 = re.search(r'.*(\d+)', num).group(1)  # 删除后员工数
        self.assertEqual(int(number_sum_3), int(self.staff_num2[0]) - 1)
        Login.save_img(self, 'test_add_6')
        time.sleep(2)

    @classmethod
    def tearDownclass(self):
        # webdriver.Chrome().quit()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
