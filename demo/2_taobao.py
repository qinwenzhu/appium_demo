# -*- coding:utf-8 -*-
# @Time: 2020/6/4 10:34
# @Author: wenqin_zhu
# @File: 2_taobao.py
# @Software: PyCharm

from appium import webdriver


des_cpas = {}

# 自动化测试的引擎，默认为 Appium，也可以指定为 Uiautomator2
des_cpas["automationName"] = "Appium"

# 使用的手机操作系统，可选择 iOS, Android
des_cpas["platformName"] = "Android"

# 手机操作系统的版本。 查看方式：设置 - 关于手机
des_cpas["platformVersion"] = "5.1.1"

# 使用的手机或模拟器类型<设备名称> 在 Andorid手机 上虽然这个参数目前已被忽略，但仍然需要添加上该参数
# 例如 127.0.0.1:62001
des_cpas["deviceName"] = "127.0.0.1:62001"

# 在当前 session 下不会重置应用的状态。默认值为 false<默认状态是重置的>，设置不重置的话，值为True
des_cpas["noReset"] = True

# TODO Android 操作系统独有的参数配置


# 查看 app包名 和 app入口 的命令：  aapt dump badging 目录路径。    如:   aapt dump badging D:\xx.apk
"""
命令：
aapt dump badging D:\taobao4android_1582098637074.apk

得到包名和入口：
package: name='com.taobao.taobao' versionCode='290' versionName='9.8.0' compileSdkVersion='28' compileSdkVersionCodename='9'
launchable-activity: name='com.taobao.tao.welcome.Welcome'  label='' icon=''
"""
# 运行的 Android 应用的包名
des_cpas["appPackage"] = "com.taobao.taobao"
# Activity 的名字是指从你的包中所要启动的 Android acticity。 <app的入口>
des_cpas["appActivity"] = "com.taobao.tao.welcome.Welcome"


# TODO 启动 app
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cpas)
