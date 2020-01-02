from selenium import webdriver
# from framework.login import Login
# # from common.chrome_browser import driver
# import time
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


class OverView(BasePage):
    count_event = '//*[@id="app"]/section/section/section[1]/div[2]/div[2]/p[1]'

    def __init__(self, driver):
        self.driver = driver

    def get_count_event(self):
        return int(self.my_find_ele_wait('xpath', self.count_event).text)


if __name__ == '__main__':
    # unittest.main()
    overView = OverView(webdriver.Firefox())
