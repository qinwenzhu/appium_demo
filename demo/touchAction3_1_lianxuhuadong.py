# -*- coding:utf-8 -*-
# @Time: 2020/6/5 17:07
# @Author: wenqin_zhu
# @File: touchAction3_1_lianxuhuadong.py.py
# @Software: PyCharm
# -*- coding:utf-8 -*-
# @Time: 2020/6/5 15:17
# @Author: wenqin_zhu
# @File: touchAction3_lianxuhuadong.py
# @Software: PyCharm

from appium import webdriver
# 导入显性等待、异常、元素定位方式
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TODO 列表滑动并找到指定的元素并进行点击操作
class AppLemon(object):

    def __init__(self, driver):
        # TODO 启动 app
        self.driver = driver
        # 显性等待
        self.wait = WebDriverWait(self.driver, 30)

    def slide_list(self):
        # 滑动列表

        # 获取当前设备的宽高
        device_size = self.driver.get_window_size()
        self.driver.swipe(start_x=device_size["width"] * 0.5, start_y=device_size["height"] * 0.9,
                     end_x=device_size["width"] * 0.5,
                     end_y=device_size["height"] * 0.1, duration=200)

    def slide_list_and_click_content(self):
        # 从首页点击到目标操作页面       # 进入首页后，点击题库元素
        loc1 = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_tiku')
        self.wait.until(EC.visibility_of_element_located(loc1))
        self.driver.find_element(*loc1).click()      # 点击题库元素定位，进入到题库页面

        # 滑动之前获取当前屏幕的源码, 在滑动操作执行之后再次进行获取源码操作，如果源码完全一致，那么判定列表已经滑动到页面的底部
        old_code = self.driver.page_source

        # 显性等待第一屏的列表加载完成后进行滑动
        loc2 = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_category_type')
        self.wait.until(EC.visibility_of_all_elements_located(loc2))

        # 滑动的同时找到对应的列表标题进行点击进入    # 找到目标元素
        loc3 = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiSelector().resourceId("com.lemon.lemonban:id/fragment_category_type").text("逻辑思维题")')
        # self.wait.until(EC.visibility_of_element_located(loc3))

        if self.wait.until(EC.visibility_of_element_located(loc3)):
            self.driver.find_element(*loc3).click()
        else:
            # 先进行第一次的列表滑动
            self.slide_list()
            self.wait.until(EC.visibility_of_all_elements_located(loc2))
            new_code = self.driver.page_source
            while True:
                if old_code == new_code or self.wait.until(EC.visibility_of_element_located(loc3)):
                    # 跳出循环滑动列表操作
                    self.driver.find_element(*loc3).click()
                    break
                else:
                    # 继续滑动列表
                    self.slide_list()


if __name__ == '__main__':
    des_cpas = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "appPackage": "com.lemon.lemonban",
        "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
        "deviceName": "127.0.0.1:62001",
        "noReset": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cpas)
    AppLemon(driver).slide_list_and_click_content()
