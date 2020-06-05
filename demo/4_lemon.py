# -*- coding:utf-8 -*-
# @Time: 2020/6/5 15:46
# @Author: wenqin_zhu
# @File: 4_lemon.py
# @Software: PyCharm


from appium import webdriver

des_cpas = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
    "deviceName": "127.0.0.1:62001",
    "noReset": True
}
# TODO 启动 app
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cpas)
