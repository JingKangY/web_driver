from time import sleep

import allure
from selenium import webdriver
from loging.log import *


class GetDriver:
    # 设置类属性
    def __init__(self):
        self.driver = None

    # 获取driver
    @allure.step('前置获取driver')
    def get_driver(self, url, browser):
        if self.driver is None:
            # 实例化浏览器
            if browser == 'Chrome':
                self.driver = webdriver.Chrome()
            if browser == 'Firefox':
                self.driver = webdriver.Firefox()
            if browser == 'Edge':
                self.driver = webdriver.Edge()
            self.driver.maximize_window()
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
