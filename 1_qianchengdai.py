# -*- coding:utf-8 -*-
# @Time: 2020/6/4 14:09
# @Author: wenqin_zhu
# @File: 1_qianchengdai.py
# @Software: PyCharm


from appium import webdriver


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

loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").index(3)')
# 显性等待
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc))
# 定位app下标 我  并进行点击
driver.find_element(*loc).click()
# driver.find_element_by_android_uiautomator('new Uiselector().className("android.widget.LinearLayout").index(3)')
# 输入手机号
driver.find_element_by_id("com.xxzb.fenwoo:id/et_phone").send_keys("18500989876")
# 点击下一步
driver.find_element_by_id("com.xxzb.fenwoo:id/btn_next_step").click()
