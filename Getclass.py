#!/usr/bin/env python
# -*- coding:utf-8 -*-
#coder:郑宇星
#date:18/7/31

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()

class Spider:
    def __init__(self,browser,email,password):
        self.url = 'http://sso.jwc.whut.edu.cn/Certification//toIndex.do'
        self.browser = browser
        self.email = email
        self.password = password
    def login(self):
        self.browser.get(self.url)
        try:
            email = WebDriverWait(self.browser,10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#textfield"))
            )
            password = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#textfield2"))
            )
            submit = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > div:nth-child(7) > button"))
            )
            email.send_keys(self.email)
            password.send_keys(self.password)
            submit.click()
        except TimeoutException:
            print('连接超时，已退出')


def main():
    email = input('请输入你的账号：')
    password = input('请输入你的密码：')
    spider = Spider(browser,email,password)
    spider.login()

if __name__ == '__main__':
    main()