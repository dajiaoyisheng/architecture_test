""" 配置文件 """
from selenium import webdriver
# _chrome_zt 1:chrome有界面、0:无界面
_chrome_zt = 1


def IsOpenBrower(self):
    if _chrome_zt == 1:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # implicitly_wait 隐式等待，单位：s ，当使用了隐士等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常。
        self.driver.implicitly_wait(10)
    elif _chrome_zt == 0:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # selenium_chrome_driver_path = ""    # chromedriver 存放的路径
        self.driver = webdriver.Chrome(chrome_options=options)   # 可添加path参数
    return self.driver


configInfo = {
    # 被测试项目的信息

    # 网址
    'url_test': 'https://www.baidu.com/',
    # 用户名、密码(joinshare)
    'userInfo': {
        'user': '15911061917',
        'pwd': 'zh@123456'
    },
    # bug管理工具redmine用户信息
    'redmineInfo': {
        'user': 'chenjindong',
        'pwd': 'jiuqi@385083'
    },
    # 发送测试报告的邮箱信息
    'emailInfo_send': {
        'username': '840758102@qq.com',
        'passwd': 'zmxspyypvagsbbbf'
    },
    # 接受测试报告的邮箱
    'emailInfo_receive': ['webdong@163.com', '269383567@qq.com', 'lishuang0902@163.com']
}
# global configInfo
