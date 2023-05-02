from time import sleep

import allure
from selenium import webdriver
from loging.log import *


class GetDriver:
    # 设置类属性
    def __init__(self):
        self.driver = None

    # 设置optionsfangshi
    def add_options(self):
        log.debug('初始化options')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # 无浏览器模式
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('----disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速
        chrome_options.add_argument("--remote-debugging-port=9222")  # this
        # chrome_options.add_argument('--start-maximized')  # 浏览器最大化
        chrome_options.add_argument('--window-size=1920x1080')  # 设置浏览器分辨率（窗口大小）
        # options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        # options.add_argument('log-level=3')
        return chrome_options

    # 获取driver
    @allure.step('前置获取driver')
    def get_driver(self, url, browser):
        if self.driver is None:
            # 最大化运行（全屏窗口）,不设置，取元素会报错
            options = self.add_options()
            # 实例化浏览器
            if browser == 'Chrome':
                self.driver = webdriver.Chrome(options=options)
            if browser == 'Firefox':
                self.driver = webdriver.Firefox(options=options)
            if browser == 'Edge':
                self.driver = webdriver.Edge(options=options)
            # self.driver.set_window_size(1920, 1080)  # 无界面模式使用
            # self.driver.maximize_window() # 有界面使用方法
            self.driver.get(url)
            log.info(f'=================获取url:{url}成功=================')
        return self.driver

    # 退出driver
    @allure.step('后置关闭driver')
    def quit_driver(self):
        if self.driver:
            sleep(1)
            self.driver.quit()
            # print("关闭之后：", driver)
            log.info("=======================class后置浏览器驱动对象已关闭=======================")
            # 注意：此处有一个很大坑
            self.driver = None
            # print("置空之后：", driver)


if __name__ == '__main__':
    # 第一次获取浏览器
    print(GetDriver().get_driver())
    # 第二次获取浏览器
    # 调用关闭，测试 关闭后driver是否为None
    GetDriver().quit_driver()
    # print(GetDriver().get_driver())
