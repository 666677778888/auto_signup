#!/usr/bin/env python
import os
from selenium import webdriver
import time
import subprocess


def doLogin():
    url = "http://192.168.168.168"
    username = "用户名"
    password = "密码"

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(0.5)

    driver.find_element_by_id('username').send_keys(username)  # 自动敲入用户名
    driver.find_element_by_id('password').send_keys(password)  # 自动敲入用户名
    driver.find_element_by_id('submit').click()  #模拟点击登录
    driver.close()


def ping():
        fnull = open(os.devnull, 'w')
        return1 = subprocess.call('ping www.tianya.cn', shell = True, stdout = fnull, stderr = fnull)
        try:
            if return1:
                    print('Internet not connected!')
                    print('Connecting now...')
                    doLogin()
            else:
                print("There is no problem")
        except:
            ping()
        fnull.close()


def __main__():
    time.sleep(60*5)
    ping()
    pass