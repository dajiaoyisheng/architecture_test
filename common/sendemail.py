# coding=utf8

import smtplib
from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from HTMLTestRunner import HTMLTestRunner
from email.header import Header
# import unittest
# import time
import os

# from common.my_logger import logger


class Email(object):

    # ==============定义发送邮件 ===============

    def send_mail(self, file_new):
        print('发送html内容文件')
        f = open(file_new, 'rb')
        # 读取测试报告正文
        mail_body = f.read()
        f.close()
        smtpserver = 'smtp.qq.com'  # 发送邮箱服务器
        # 发送邮箱用户/密码(登录邮箱操作)
        username = '840758102@qq.com'
        passwd = 'zmxspyypvagsbbbf'
        # sender = '840758102@qq.com'  # 发送邮箱
        receiver = ['webdong@163.com']  # 接收邮箱

        subject = ' joinshare自动化测试报告'  # 发送主题

        msg = MIMEText(mail_body, 'html', 'utf-8')

        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = username
        msg['To'] = ",".join(receiver)

        # 连接发送邮件
        try:
            smtp = smtplib.SMTP(smtpserver, 587)
            smtp.starttls()
            smtp.login(username, passwd)  # 登录邮箱
            smtp.sendmail(username, receiver, msg.as_string())  # 发送者和接收者
        except Exception as msg:
            print('邮件发送失败！', msg)
        else:
            print('邮件发送成功！')
        finally:
            smtp.quit()

    # ======================查找最新的测试报告==========================

    def new_report(self, testreport):
        lists = os.listdir(testreport)
        lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
        file_new = testreport + '/' + lists[-1]
        return file_new


if __name__ == '__main__':
    pass
