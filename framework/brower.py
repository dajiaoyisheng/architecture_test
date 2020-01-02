# 打开浏览器
# codeing=utf-8
# from selenium import webdriver


class HandlerBrower(object):
    def __init__(self, driver):
        self.driver = driver
        self.open()

    def open(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()
