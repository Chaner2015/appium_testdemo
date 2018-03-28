# -*- coding: UTF-8 -*-

# @Time    : 2018/3/6 下午4:53
# @Author  : lily
# @File    : test_kalaok_activity.py
# @PROJECT_NAME : Pythoncoding

import unittest
from time import sleep
from appium import webdriver

class Activity(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "android"
        desired_caps["deviceName"] = "vivoX5play"
        desired_caps["appPackage"] = "com.audiocn.kalaok"
        desired_caps["appActivity"] = "com.audiocn.common.activity.WelcomActivity"
        desired_caps["noReset"] = "true"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        print("测试结束，清理环境ing")

    def test_activity(self):
        sleep(10)
        try:
            self.driver.find_element_by_xpath("//*[@text='活动']").click()
            # switch to webview
            print('contexts:', self.driver.contexts)    # 会打印出两个值
            # webview = self.driver.switch_to.context("NATIVE_APP")   # 传入web的
            self.driver.back()
        except Exception as e:
            print("未找到", e)




if __name__=='__main__':
    unittest.main()