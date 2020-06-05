# -*- coding:utf-8 -*-
# @Time: 2020/6/5 14:06
# @Author: wenqin_zhu
# @File: 3_baiduMap.py
# @Software: PyCharm

from appium import webdriver

des_cpas = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "appPackage": "com.baidu.BaiduMap",
    "appActivity": "com.baidu.baidumaps.WelcomeScreen",
    "deviceName": "127.0.0.1:62001",
    "noReset": True
}
# TODO 启动 app
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cpas)
