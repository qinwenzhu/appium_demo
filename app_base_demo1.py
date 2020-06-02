# -*- coding:utf-8 -*-
# @Time: 2020/5/29 11:33
# @Author: wenqin_zhu
# @File: app_base_demo1.py
# @Software: PyCharm


from appium import webdriver

# 设置参数方式一:
# des_cap = {
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "appPackage": "com.xxzb.fenwoo",
#     "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
#     "deviceName": "127.0.0.1:62001",
#     "noReset": True
# }

# 设置参数方式二:
des_cap = {}

# des_cap["automationName"] = "Appium"      # 默认为appium
# 设置操作系统和对应的版本
des_cap["platformName"] = "Android"
des_cap["platformVersion"] = "5.1.1"

# 设置设备名称
des_cap["deviceName"] = "127.0.0.1:62001"
# des_cap["deviceName"] = "emulator-5554"

# 通过以下命令获取到当前需要操作的包名和app入口
# aapt dump badging <应用app的路径>          # aapt dump badging "D:/Future-release-2018.apk"
# TODO 前程贷apk
# des_cap["appPackage"] = "com.xxzb.fenwoo"
# des_cap["appActivity"] = "com.xxzb.fenwoo.activity.addition.WelcomeActivity"

# TODO 百度地图
des_cap["appPackage"] = "com.baidu.BaiduMap"
des_cap["appActivity"] = "com.baidu.baidumaps.WelcomeScreen"


# 设置不重置app数据，默认为true
des_cap["noReset"] = True

# 启动对应的app
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cap)
