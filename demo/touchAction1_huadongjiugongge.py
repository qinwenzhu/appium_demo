# -*- coding:utf-8 -*-
# @Time: 2020/6/5 10:25
# @Author: wenqin_zhu
# @File: touchAction1_huadongjiugongge.py
# @Software: PyCharm


from appium import webdriver
# 手机单点触碰
from appium.webdriver.common.touch_action import TouchAction
# 手机多点触碰
# from appium.webdriver.common.multi_action import MultiAction
# 导入显性等待、异常、元素定位方式
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

des_cpas = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "appPackage": "com.xxzb.fenwoo",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "deviceName": "127.0.0.1:62001",
    "noReset": True
}
# TODO 启动 app
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cpas)
# 显性等待
wait = WebDriverWait(driver, 30)


# TODO 拓展：获取当前手机的屏幕宽高
# size = driver.get_window_size()
# print(size)  # {'width': 720, 'height': 1280}

# 获取密码框区域的元素
loc = (MobileBy.ID, 'com.xxzb.fenwoo:id/lpv_password')
wait.until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)
# 获取密码框的宽高
ele_size = ele.size
print(ele_size)    # {"width":630,"height":630}

# 获取密码框的起点坐标
start_point = ele.location
print(start_point)    # {"x":45,"y":329}


# 大致将九宫格的横向距离等分 - 将整个手机的横向分成6份，每一个等份都为一个正方形。根据每个正方形的坐标进行坐标的点移动
# 计算每一等份的步长
step = ele_size["width"]/6
print(step)

# 按照用户设置的九宫格密码走向计算对应的步长
p1 = (start_point["x"]+step, start_point["y"]+step)
p2 = (start_point["x"]+step*3, start_point["y"]+step)
p3 = (start_point["x"]+step*5, start_point["y"]+step)
p4 = (start_point["x"]+step*3, start_point["y"]+step*3)
p5 = (start_point["x"]+step*3, start_point["y"]+step*5)

touch = TouchAction(driver)
# 按压的第一个点为：按压   备注：只能选择按压特定的元素或者是指定点的坐标
touch.press(el=None, x=p1[0], y=p1[1]).wait(200)     # press / wait
# 移动到第二个点： move_to / wait
touch.move_to(x=p2[0], y=p2[1]).wait(200)
touch.move_to(x=p3[0], y=p3[1]).wait(200)
touch.move_to(x=p4[0], y=p4[1]).wait(200)
touch.move_to(x=p5[0], y=p5[1]).wait(200)
# 依次类推，直到移动到最后一个点的后续操作： 释放 release / wait
# …… touch.move_to()
touch.release().wait(200)
# 最后执行前面的所有动作
touch.perform()
