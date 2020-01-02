# -*- coding: utf-8 -*-
import os
import unittest
import time
from common.sendemail import Email
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
# from BeautifulReport import BeautifulReport


def _main():
    print('========== START ==========')
    testdir = os.path.dirname(os.path.dirname(__file__))
    test_dir = os.path.join(testdir, 'test_case')  # 测试用例文件夹
    # log_dir = os.path.join(testdir, 'logs')  # 测试用例文件夹
    test_report = testdir + '/report'
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    report_file_name = 'result_' + now + '.html'
    report_file_dir = test_report + '/' + report_file_name
    fp = open(report_file_dir, 'wb')
    # stream放生成报告的路径
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='case_*.py')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description='用例执行情况：')
    runner.run(discover)
    # 在邮件中没有内容

    # result = BeautifulReport(discover)
    # result.report(filename=report_file_name, description='joinshare自动化测试报告', report_dir=test_report, log_path='')  # 默认在当前路径下，可以加log_path

    fp.close()
    email = Email()
    new_report = email.new_report(test_report)
    email.send_mail(new_report)
    print('========== END ==========')
    # 在浏览器中打开测试报告
    driver = webdriver.Chrome()
    print(report_file_dir)
    driver.get(report_file_dir)
    # driver.get('c:/Users/jiuqi/Desktop/joinshare_test/joinshare_test/report/result_2019-12-31 11_14_49.html')


if __name__ == "__main__":
    _main()
