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
# 在配置文件中  把路径直接加上了
# from common.my_logger import logger
from framework.base_page import BasePage


class MyEvent(BasePage):

    count_all_loc = '//*[@id="app"]/section/section/section/div[1]/ul/li[2]/a/span'  # 全部数量
    name_event_loc = '//*[@id="app"]/section/section/section/div[2]/table/tbody/tr[2]/td[1]/div/a/span'  # 第一条数据的活动名称
    ope_eles_loc = '//*[@id="app"]/section/section/section/div[2]/table/tbody/tr[2]/td[7]/div/a'  # 列表操作项所有元素
    more_eles_loc = '/html/body/div[2]/section/section/section/div[2]/table/tbody/tr[2]/td[7]/div/a[4]/ul/li'  # 更多下拉框中的所有元素,只在操作项有4条时

    del_event_loc = '/html/body/div[2]/section/section/section/div[2]/table/tbody/tr[2]/td[7]/div/a[4]/ul/li[5]'  # 删除活动
    del_confirm_loc = '/html/body/div[4]/div[3]/a[1]'
    pub_confirm_loc = '/html/body/div[4]/div[3]/a[1]'  # 发布弹层确定
    view_pre_loc = '//*[@id="app"]/section/section/section/div[2]/table/tbody/tr[2]/td[7]/div/a[3]'  # 预览
    line_down_loc = '//*[@id="app"]/section/section/section/div[2]/table/tbody/tr[2]/td[7]/div/a[1]'  # 下线
    creat_btn_loc = '//*[@id="app"]/section/section/section/div[1]/div/a'

    def __init__(self, driver):
        self.driver = driver

    def get_name_first_event(self):
        time.sleep(5)
        return self.my_find_ele_wait('xpath', self.name_event_loc).text

    def count_event(self):
        return self.my_find_ele_wait('xpath', self.count_all_loc).text

    def list_ope(self, action):
        time.sleep(1)
        eles_ope = self.driver.find_elements_by_xpath(self.ope_eles_loc)
        for ele in eles_ope:
            text = ele.text
            if text == action:
                ele.click()
                break

    def pub_confirm(self):
        self.my_find_ele_wait('xpath', self.pub_confirm_loc).click()

    def ope_first_text(self):
        return self.my_find_ele_wait('xpath', self.line_down_loc).text

    # 点击更多，下拉框中的操作
    def handler_more(self, action):
        time.sleep(1)
        eles_more = self.driver.find_element_by_xpath(self.more_eles_loc)
        for ele in eles_more:
            text = ele.text
            if text == action:
                ele.click()
                break

    def del_confirm(self):
        self.my_find_ele_wait('xpath', self.del_confirm_loc).click()

    def test_event_creat(self):
        self.my_find_ele_wait('xpath', self.creat_btn_loc).click()
        pass


if __name__ == '__main__':
    # unittest.main()
    myevent = MyEvent(webdriver.Firefox())
