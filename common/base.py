# -*-coding = utf-8 -*-
'''
@File    :  base.py
@Time    :  2023/4/8 20:11
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  base
'''
import time

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from loging.log import log


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver
        # 临时代替driver
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option("detach", True)
        # self.driver = webdriver.Chrome(chrome_options=option)

    # 查找元素方法 (提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc),
                                                                                      message=f'查找元素：{loc}报错')

    # 刷新方法
    @allure.step('刷新')
    def base_renovate(self, loc):
        self.base_find_element(loc).refrensh()

    # 刷前进后退方法 ，如过要定位元素还需要刷新页面
    @allure.step('前进后退')
    def base_forward_or_back(self, forward_or_back):
        if forward_or_back == 'forward':
            self.driver.forward()
        if forward_or_back == 'back':
            self.driver.back()

    # 点击方法
    @allure.step('点击')
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    @allure.step('输入相关参数')
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 删除输入框内容
    @allure.step("删除输入框内容")
    def base_delete(self, loc):
        el = self.base_find_element(loc)
        # 清空
        el.clear()

    # 获取文本方法
    def base_get_element_text(self, loc):
        # 注意：一定要返回元素的文本信息
        return self.base_find_element(loc).text

    # 获取当前页面的URL
    @allure.step('获取当前页面的URL')
    def base_get_current_url(self):
        return self.driver.current_url

    # 截图方法
    def base_get_image(self):
        # image_path = GetFilePath().get_all_file_path(r'image/')
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 获取截图添加到allure报告中
    def base_get_png_path_to_allure(self):
        pass

    # 切换到最新的handle
    @allure.step('切换到新的窗口')
    def base_switch_to_new_handle(self):
        # self.base_find_element(loc)
        self.current_handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        time.sleep(2)

    # 切换到默认的handle
    @allure.step('切换到主窗口')
    def base_switch_to_current_handle(self):
        self.driver.switch_to.window(self.current_handle)
        time.sleep(2)

    # 3、double_and_drop(source, target)  # 拖拽
    # 4、move_to_element(element)  # 悬停 【重点】
    # 5、perform()  # 执行以上事件的方法 【重点】
    @allure.step('右击、双击')
    def base_right_or_double_click(self, loc, click_method):
        action = ActionChains(self.driver)
        el = self.base_find_element(loc)
        if click_method == 'right':
            action.context_click(el).perform()
        if click_method == 'double':
            action.double_click(el).perform()
        time.sleep(0.5)

    # 悬停在指定元素位置
    @allure.step('悬停指定元素位置')
    def base_move_to_element(self, loc):
        action = ActionChains(self.driver)
        el = self.base_find_element(loc)
        action.move_to_element(el).perform()
        time.sleep(0.5)

    @allure.step("组合键keys值输入")
    def base_send_keys(self, loc, key):
        """
        :param loc: 元素
        :param key: 根据输入的快捷键选择对应的方法
        :return:
        """
        el = self.base_find_element(loc)
        if key == 'BACK_SPACE':
            el.send_keys(Keys.BACK_SPACE)
        elif key == 'SPACE':
            el.send_keys(Keys.SPACE)
        elif key == 'TAB':
            el.send_keys(Keys.TAB)
        elif key == 'ESCAPE':
            el.send_keys(Keys.ESCAPE)
        elif key == 'ENTER':
            log.debug('执行成功')
            el.send_keys(Keys.ENTER)
        elif key == 'F1':
            el.send_keys(Keys.F1)
        elif key == 'F5':
            el.send_keys(Keys.F5)
        elif key == 'F12':
            el.send_keys(Keys.F12)
        else:
            log.error('组合键类型错误，请重新输入')

    # 键盘control 组合键输入
    @allure.step("键盘control 组合键key值输入")
    def base_send_keys_control(self, loc, key):
        """
        :param loc: 元素
        :param key: control 组合键
        :return:
        """
        el = self.base_find_element(loc)
        el.send_keys(Keys.COMMAND, key)  # MAC用command win 用control

    # 判断元素是否被选中 选中true 未选中false
    @allure.step("判断当前元素是否被选中")
    def base_element_is_selected(self, loc):
        el = self.base_find_element(loc)
        return el.is_selected()

    # 判断元素是否可见 选中true 未选中false
    @allure.step("判断当前元素是否可见")
    def base_element_is_displayed(self, loc):
        el = self.base_find_element(loc)
        return el.is_displayed()

    # 判断元素是否可用 选中true 未选中false
    @allure.step("判断当前元素是否可用")
    def base_element_is_enabled(self, loc):
        el = self.base_find_element(loc)
        return el.is_enabled()

    # 封装判断元素是否存在的方法
    @allure.step('判断当前元素是否存在')
    def base_element_if_exist(self, loc):
        try:
            # 找到元素
            self.base_find_element(loc, timeout=2)
            return True
        except:
            # 没有找到元素
            return False
