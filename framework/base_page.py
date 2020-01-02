# -*- coding: utf-8 -*-
"""
    @desc: object测试基类
    @file: base_page.py
    @date: 2018/11/19
"""
from common.my_logger import logger
# from random import choice
from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import os
# import time
from common.my_redmine import link_redmine
UI_WAIT_TIME = 20


# BasePage封装所有页面都公用的方法，例如driver, url ，FindElement等
class BasePage(object):
    redmine_user = 'chenjindong'
    redmine_pwd = 'jiuqi@385083'

    def __init__(self, driver):
        self.driver = driver
        # self.driver.implicitly_wait(20)

    def _loading(self, type, loc):
        try:
            # loading出现
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(
                    (By.ID, 'layui-layer-shade1')))
            # loading消失
            WebDriverWait(self.driver, 30).until_not(
                EC.visibility_of_element_located(
                    (By.ID, 'layui-layer-shade1')))
        except (NoSuchElementException, TimeoutException):
            # self._driver.quit()
            logger.error('[{}]寻找元素失败, 定位方式为{}:{}'.format(
                os.path.basename(__file__), type, loc))
            raise TimeoutException(msg='[{}]寻找元素失败, 定位方式为{}:{}'.format(
                os.path.basename(__file__), type, loc))

    # 等待页面loading结束
    def _wait(self, type, loc):
        '''
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        '''
        try:
            if type == 'xpath':
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, loc)))
            elif type == 'id':
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID, loc)))
            elif type == 'css':
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, loc)))
            # return self.driver.find_element_by_xpath(loc).click()
        except (NoSuchElementException, TimeoutException):
            logger.error('[{}]寻找元素失败, 定位方式为{}:{}'.format(
                os.path.basename(__file__), type, loc))
            raise TimeoutException(msg='[{}]寻找元素失败, 定位方式为{}:{}'.format(
                os.path.basename(__file__), type, loc))

    # 获取元素
    def _find_ele(self, type, loc):
        if type == 'xpath':
            return self.driver.find_element_by_xpath(loc)
        elif type == 'id':
            return self.driver.find_element_by_id(loc)
        elif type == 'css':
            return self.driver.find_element_by_css_selector(loc)

    # 查找元素，等待页面loading出现后再消失，避免因loading层而点击不到元素。
    def my_find_ele_load(self, type, loc):
        self._loading(type, loc)
        return self._find_ele(type, loc)

    # 在操作后需要等待的
    def my_find_ele_wait(self, type, loc):
        self._wait(type, loc)
        return self._find_ele(type, loc)

    '''
    @type_assert:断言方式
    @method_assert:该断言方式的方法
    @value_real:真实的结果
    @value_except:期待的结果
    @subject_redmine:remine问题的主题
    @des_redmine:remine问题的描述
    '''

    def my_assert(self, type_assert, method_assert, value_real, value_except,
                  subject_redmine, des_redmine):
        if type_assert == 'assertTrue':
            try:
                method_assert(value_real == value_except, msg=des_redmine)
            except Exception as des_redmine:
                data = {
                    "subject": '[自动创建]' + subject_redmine,
                    "description": des_redmine
                }
                link_redmine(self.redmine_user, self.redmine_pwd, data)
                method_assert(value_real == value_except, msg=des_redmine)
