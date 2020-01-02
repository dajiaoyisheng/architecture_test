import unittest
# from selenium import webdriver
from framework.login import Login
# import os
import time
# from common.my_redmine import link_redmine
# from common.chrome_browser import driver
# from selenium.webdriver.chrome.options import Options
# from common.my_logger import logger
from framework.newevent_page import NewEvent
from framework.base_page import BasePage
from framework.myevent_page import MyEvent
from framework.overview_page import OverView
from config.cofig import userInfo
from config.cofig import IsOpenBrower
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class MyEventList(unittest.TestCase):
    url_page_creat = 'https://manage.joinshare.newssdk.com/act/templatelist'

    @classmethod
    def setUpClass(cls):
        # chrome_options = Options()
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--headless')
        # cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        # cls.driver = webdriver.Chrome()
        cls.driver = IsOpenBrower(cls)
        # cls.driver = webdriver.Firefox()
        cls.baseFn = BasePage(cls.driver)
        # Login(cls.driver)
        Login.login(cls, userInfo['user'], userInfo['pwd'])
        time.sleep(10)
        cls.neweventFn = NewEvent(cls.driver)
        cls.myeventFn = MyEvent(cls.driver)
        cls.overViewFn = OverView(cls.driver)
        # 进入我的活动页面
        cls.driver.get('https://manage.joinshare.newssdk.com/act/list')
        cls.redmine_user = 'chenjindong'
        cls.redmine_pwd = 'jiuqi@385083'
        # warnings.simplefilter("ignore", ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.driver.quit()

    # 点击新建活动按钮
    def test_event_creat_btn(self):
        '''在我的活动页面点击新建活动按钮'''
        time.sleep(10)
        self.myeventFn.test_event_creat()
        time.sleep(10)
        msg = '在我的活动页面点击新建活动失败'
        self.baseFn.my_assert('assertTrue', self.assertTrue,
                              self.driver.current_url, self.url_page_creat,
                              '创建活动异常', msg)


if __name__ == '__main__':
    unittest.main()
