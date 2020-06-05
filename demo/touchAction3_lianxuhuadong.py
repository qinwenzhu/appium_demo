# -*- coding:utf-8 -*-
# @Time: 2020/6/5 15:17
# @Author: wenqin_zhu
# @File: touchAction3_lianxuhuadong.py
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
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
    "deviceName": "127.0.0.1:62001",
    "noReset": True
}
# TODO 启动 app
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cpas)
# 显性等待
wait = WebDriverWait(driver, 30)

# TODO列表滑动并找到指定的元素并进行点击操作

# 进入首页后，点击题库元素
loc = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 显性等待第一屏的列表加载完成后进行滑动
loc = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_category_type')
wait.until(EC.visibility_of_all_elements_located(loc))

# 滑动之前获取当前屏幕的源码, 在滑动操作执行之后再次进行获取源码操作，如果源码完全一致，那么判定列表已经滑动到页面的底部
# driver.page_source()

# 滑动列表
# 获取当前设备的宽高
device_size = driver.get_window_size()
driver.swipe(start_x=device_size["width"]*0.5, start_y=device_size["height"]*0.9, end_x=device_size["width"]*0.5,
             end_y=device_size["height"]*0.1, duration=200)

wait.until(EC.visibility_of_all_elements_located(loc))
# new_code = driver.page_source()

# 滑动的同时找到对应的列表标题进行点击进入
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.lemon.lemonban:id/fragment_category_type").text("逻辑思维题")')
wait.until(EC.visibility_of_element_located(loc))
wait.until(EC.element_to_be_clickable(loc))
driver.find_element(*loc).click()
code = driver.page_source()
print(code)

while True:
    if old_code == new_code or wait.until(EC.element_to_be_clickable(loc)):
        # 跳出循环滑动列表操作
        break
    else:
        # 继续滑动列表
        driver.swipe(start_x=device_size["width"] * 0.5, start_y=device_size["height"] * 0.9,
                     end_x=device_size["width"] * 0.5,
                     end_y=device_size["height"] * 0.1, duration=200)


class AppLemon(object):
    def __init__(self):
        self.driver = webdriver.Remote()

    def slide_list_content(self):
        # 从首页点击到目标操作页面
        pass
