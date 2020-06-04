# -*- coding:utf-8 -*-
# @Time: 2020/6/4 13:49
# @Author: wenqin_zhu
# @File: element_positioning_mode.py
# @Software: PyCharm

# 所有浏览器共用的 WebDriver 类
from appium import webdriver


class AppDemo:

    def __init__(self):
        self.driver = webdriver.Remote()

    # 通过 app resource_id  定位元素
    def get_ele_loc_by_resource_id(self):
        self.driver.find_element_by_id("resource_id")

    # 通过 uiautomator 框架中的 UiSelector 的 text()方法
    def get_ele_loc_by_uiautomator_text(self, text):
        self.driver.find_element_by_android_uiautomator(f"new UiSelector().text({text})")
