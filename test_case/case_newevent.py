import unittest

# from selenium import webdriver
from framework.login import Login
# import os
import time
# from common.my_redmine import link_redmine
# from common.chrome_browser import driver
# from common.my_logger import logger
from framework.newevent_page import NewEvent
from framework.base_page import BasePage
from framework.myevent_page import MyEvent
from framework.overview_page import OverView
from config.cofig import userInfo
from config.cofig import IsOpenBrower
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class CaseNewEvent(unittest.TestCase):

    h1_event_text = '自动化测试填写主题'
    name_event_text = '自动化测试填写名称'
    count_all_event_del = 0
    # def __init__(self):
    #     self.h1_event_text = '自动化测试填写主题'
    #     self.name_event_text = '自动化测试填写名称'
    #     self.count_all_event_del = 0

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome()
        cls.driver = IsOpenBrower(cls)
        cls.baseFn = BasePage(cls.driver)
        # Login(cls.driver)
        Login.login(cls, userInfo['user'], userInfo['pwd'])
        time.sleep(10)
        cls.neweventFn = NewEvent(cls.driver)
        cls.myeventFn = MyEvent(cls.driver)
        cls.overViewFn = OverView(cls.driver)
        # 登录之后通过修改url直接进入新建活动页面
        cls.driver.get(
            'https://manage.joinshare.newssdk.com/act/createactivity?template_class=7'
        )

        cls.redmine_user = 'chenjindong'
        cls.redmine_pwd = 'jiuqi@385083'
        # warnings.simplefilter("ignore", ResourceWarning)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 创建新活动
    def test_new(self):
        '''创建新活动'''
        # 通过点击左菜单进入新建活动页面
        # self.neweventFn.newevent_page()
        # 点击新建空白海报
        # self.driver.find_element_by_xpath('//*[@id="app"]/section/section/div[2]/div[1]/div').click()
        # 在新建的活动页面上写上主标题
        self.neweventFn.text_clk(self.h1_event_text)
        self.neweventFn.clk_like()
        time.sleep(5)
        # self.neweventFn.set_confirm()
        # 填写活动名称
        self.neweventFn.event_name(self.name_event_text)
        # 第一次点击保存
        self.neweventFn.save_clk()
        # 出现弹层
        # 点击去列表页
        self.neweventFn.topage_list()

    # 创建活动后我的活动页面数据改变
    def test_new_tomyevent(self):
        '''跳转到我的活动页面'''
        # 拿取列表页第一条数据的判断活动名称
        name_first_event = self.myeventFn.get_name_first_event()
        # self.neweventFn.myevent_list_sum()
        # self.assertTrue(name_first_event == self.name_event_text,
        #                 msg='活动列表第一条数据不是刚新建的活动')
        msg = '活动列表第一条数据不是刚新建的活动'
        self.baseFn.my_assert('assertTrue', self.assertTrue, name_first_event,
                              self.name_event_text, '我的活动页面列表数据异常', msg)

    def test_new_tomyevent_pub(self):
        '''发布活动'''
        self.myeventFn.list_ope('发布')
        time.sleep(5)
        self.myeventFn.pub_confirm()
        # 发布，等待页面更新数据
        time.sleep(5)

    def test_new_tomyevent_pub_down(self):
        '''活动下线'''
        msg = '发布活动失败'
        self.baseFn.my_assert('assertTrue', self.assertTrue,
                              self.myeventFn.ope_first_text(), '下线', '发布活动异常',
                              msg)
        # try:
        #     self.assertTrue(self.myeventFn.ope_first_text() == '下线', msg='发布活动失败')
        # except:
        #     data = {
        #         "subject": '[自动创建]发布活动异常',
        #         "description": '发布活动失败'
        #     }
        #     link_redmine(self.redmine_user, self.redmine_pwd, data)
        #     self.assertTrue(self.myeventFn.ope_first_text() == '下线', msg='发布活动失败')

        self.myeventFn.list_ope('预览')
        pass

    # 查看发布是否成功

    # def test_new_tomyevent_del(self):
    #     # 记录一下全部有多少条数据
    #     count_all_event = int(self.myeventFn.count_event())
    #     # 删除刚创建的活动
    #     self.myeventFn.list_ope('更多')
    #     self.myeventFn.handler_more('删除活动')
    #     self.myeventFn.del_confirm()
    #     # 此处有个请求接口
    #     time.sleep(5)
    #     # 删除后全部的计数是否减一
    #     self.count_all_event_del = int(self.myeventFn.count_event())
    #     self.assertTrue(count_all_event - 1 == self.count_all_event_del, msg='删除未成功')

    def event(self):
        pass

    # def test_new_myevent_01(self):
    #     for i in range(20):
    #         time.sleep(5)
    #         self.myeventFn.list_ope('更多')
    #         self.myeventFn.handler_more('删除活动')
    #         self.myeventFn.del_confirm()

    # 去概览页查看活动数量是否改变
    # def test_new_tomyevent_del_overview(self):
    #     self.driver.get('https://manage.joinshare.newssdk.com/ent/index')
    #     count_overview_event = self.overViewFn.get_count_event()
    #     self.assertTrue(self.count_all_event_del == count_overview_event, msg='删除活动后，概览页活动数量显示错误')


if __name__ == '__main__':
    unittest.main()
