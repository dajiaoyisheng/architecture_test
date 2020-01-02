from selenium import webdriver
# from framework.login import Login
# from common.chrome_browser import driver
import time
# import os
# import sys
# import unittest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# # 在配置文件中  把路径直接加上了
# from common.my_logger import logger
from framework.base_page import BasePage


class NewEvent(BasePage):
    event_menu_text_loc = '//*[@id="app"]/section/section/div[1]/div[1]/div[1]/p'  # 菜单-文字
    event_menu_text_h1_loc = '//*[@id="app"]/section/section/div[1]/div[1]/div[1]/ul/li[1]/p'  # 菜单-文字-主标题
    event_menu_text_h1_text_loc = '/html/body/div[1]/section/section/div[1]/div[3]/div/div[2]/div/div[1]/div'  # 菜单-文字-填写上新主标题
    event_menu_comt_loc = '//*[@id="app"]/section/section/div[1]/div[1]/div[5]/p'  # 菜单-组件
    event_menu_comt_like_loc = '//*[@id="app"]/section/section/div[1]/div[1]/div[5]/ul/li[1]/div'  # 菜单-组件-点赞
    set_confirm_loc = '//*[@id="eleattr"]/div[2]/a[2]'  # 菜单-组件-点赞-确定
    event_menu_comt_like_color_loc = '//*[@id="eleattr"]/div[1]/div[1]/div[4]/div/div[1]/div/div/div[1]/div[2]/div'  # 菜单-组件-点赞-颜色
    event_menu_comt_like_color_red_loc = '/html/body/div[8]/div[3]/div[1]'  # 菜单-组件-点赞-颜色-红色
    event_menu_comt_like_color_confirm_loc = '/html/body/div[6]/div[4]/div[3]/a[2]'  # 菜单-组件-点赞-颜色-确定
    event_name_loc = '//*[@id="app"]/section/section/div[2]/div/div[2]/div[1]/div/input'  # 活动名称
    topagelist_loc = '//*[@id="layui-layer2"]/div[3]/a[2]'  # 保存活动
    save_btn = '//*[@id="save-task"]'

    def __init__(self, driver):  # 代码有问题   咋不处理一下
        self.driver = driver

    # 记录我的活动列表中有多少活动，在新建后对比来判断是否成功
    def myevent_list_sum(self):
        myevent_count = self.my_find_ele_wait('xpath', '//*[@id="app"]/section/section/section/div[1]/ul/li[2]/a/span').text
        print(myevent_count)
        pass

    # 点击保存-去列表页
    def topage_list(self):
        self.my_find_ele_wait('xpath', self.topagelist_loc).click()
        pass

    # 新建活动类

    # 点击新建空白海报进入新建活动页面
    def newevent_page(self):
        # 等待loading消失后点击做活动下拉框
        self.my_find_ele_load(
            'xpath', '//*[@id="app"]/aside/div/div[2]/div/div[2]/p').click()
        # 点击下拉菜单中的新建活动进入新建活动页面
        self.my_find_ele_wait('xpath', '//*[@id="app"]/aside/div/div[2]/div/div[2]/ul/li[1]').click()
        # 等待loading消失后点击新建活动模板
        self.my_find_ele_wait('xpath', '//*[@id="app"]/section/section/div[2]/div[1]').click()

    # 点击菜单-文字 添加主标题到活动页面
    def text_clk(self, text):
        self.my_find_ele_wait('xpath', self.event_menu_text_loc).click()
        self.my_find_ele_wait('xpath', self.event_menu_text_h1_loc).click()
        self.my_find_ele_wait('xpath', self.event_menu_text_h1_text_loc).send_keys(text)
        pass

    # 点击菜单-组件
    def comt(self):
        self.my_find_ele_wait('xpath', self.event_menu_comt_loc).click()
        pass

    # 点击设置的确定
    def set_confirm(self):
        self.my_find_ele_wait('xpath', self.set_confirm_loc).click()
        pass

    def clk_like(self):
        # event_menu_comt_like_loc
        self.comt()
        self.my_find_ele_wait('xpath', self.event_menu_comt_like_loc).click()
        # 颜色
        self.my_find_ele_wait('xpath',
                              self.event_menu_comt_like_color_loc).click()
        time.sleep(2)
        # 选个红色
        self.my_find_ele_wait('xpath',
                              self.event_menu_comt_like_color_red_loc).click()
        # 选择颜色确定
        # self.my_find_ele_wait('xpath', self.event_menu_comt_like_color_confirm_loc).click()
        # 点赞组件确定
        # self.set_confirm()

    def save_clk(self):
        self.my_find_ele_wait('xpath', self.save_btn).click()
        pass

    def event_name(self, text):
        event_name_ele = self.my_find_ele_wait('xpath', self.event_name_loc)
        event_name_ele.clear()
        event_name_ele.send_keys(text)
        # if text:
        # else:

    def funcname(self):
        pass


if __name__ == '__main__':
    # unittest.main()
    newevent = NewEvent(webdriver.Firefox())
    newevent.newevent_page()
