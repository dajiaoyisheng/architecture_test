import unittest
# import time
from framework.base_page import BasePage
from framework.index_page import IndexPage
# from config.cofig import configInfo
from config.cofig import IsOpenBrower


class Index(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = IsOpenBrower(cls)
        cls.baseFn = BasePage(cls.driver)
        cls.indexPageFn = IndexPage(cls.driver)
        cls.driver.get('https://www.baidu.com/')

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        # self.driver.quit()
        pass

    # 测试用例 必须以 'test_' 开头
    def test_search(self):
        ''' 搜索 你好 '''
        self.indexPageFn.searchInputEnter('你好')
        # msg = '搜索失败'
        print(self.indexPageFn.resSearchFirst())
        # self.baseFn.my_assert('assertTrue', self.assertTrue,
        #                       self.indexPageFn.resSearchFirst(), '',
        #                       '搜索异常', msg)


if __name__ == '__main__':
    unittest.main()
