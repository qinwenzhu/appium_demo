# -*- coding:utf-8 -*-
# @Time: 2020/6/5 14:05
# @Author: wenqin_zhu
# @File: touchAction2_duodianchukong.py
# @Software: PyCharm

from time import sleep
from appium import webdriver
# 手机单点触碰
from appium.webdriver.common.touch_action import TouchAction
# 手机多点触碰
from appium.webdriver.common.multi_action import MultiAction

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

# 场景：多点触控 地图上针对当前定位的缩放和放大

# 获取当前设备的宽高
device_size = driver.get_window_size()
print(device_size)

sleep(3)

# 两个手指同时按压中心点，进行地图的放大操作
# a1的单点动作移向右上方，a2的单点动作移向左下方
a1 = TouchAction(driver).press(x=device_size["width"]*0.5, y=device_size["height"]*0.5).wait(200)\
    .move_to(x=device_size["width"]*0.7, y=device_size["height"]*0.3).wait(200).release()
a2 = TouchAction(driver).press(x=device_size["width"]*0.45, y=device_size["height"]*0.55).wait(200)\
    .move_to(x=device_size["width"]*0.2, y=device_size["height"]*0.7).wait(200).release()

# 将两个点的当点触控操作添加到多点触控类中进行连续操作
multi = MultiAction(driver)
multi.add(a1, a2)
multi.perform()
