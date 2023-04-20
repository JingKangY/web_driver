# -*-coding = utf-8 -*-
'''
@File    :  test_login.py
@Time    :  2023/4/9 21:35
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  test_login_lingxigames
'''
from time import sleep

import allure
import pytest
import conftest
from common.asserts import WebUIAssert
from common.base import Base
from common.page_elements import *
from data.get_filepath import GetFilePath


@allure.epic('测试')  # 大标题 一级目录
@allure.feature('测试')  # feature：allure报告的标题（二级目录）
# @allure.link('https://aone.alibaba-inc.com/v2/project/1073158/bug#viewIdentifier=5dfb195e2e2b84f6b2f24718')
@allure.issue('https://aone.alibaba-inc.com/v2/project/1073158/bug#viewIdentifier=5dfb195e2e2b84f6b2f24718')
# @pytest.mark.repeat(2) # 重复跑两次
class TestLogin:

    # allure.attach.file(source=(GetFilePath().get_all_file_path(r'data/双创wa项目接口文档.xlsx')),attachment_type=allure.attachment_type.name)
    #
    # @pytest.mark.bind_role
    @allure.story('测试')  # story：allure报告的三级目录
    # 缺陷等级 blocker：中断缺陷 critical:临界缺陷 normal：普通缺陷 minor：次要缺陷 trivial：轻微的缺陷
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.usefixtures('connect_db')  # 另一种调用方式 级别为class
    #  用例描述2, 接口路径5, 请求方法6, 请求类型7, 参数9,步骤11， 预期结果code12,预期结果msg13,预期结果message14,
    def test_login(self, get_quit_driver,del_image_png):
        # title, desc, url, method, request_type, args, request_head, step, expect_code, expect_mes, expect_total_count = case_info

        base = Base(get_quit_driver)
        base.base_input(sousuoshurukuang, "三国志战略版")
        base.base_send_keys_control(sousuoshurukuang, 'a')
        sleep(2)
        base.base_send_keys_control(sousuoshurukuang, 'c')
        base.base_delete(sousuoshurukuang)
        base.base_send_keys_control(sousuoshurukuang, 'v')
        sleep(2)
        base.base_click(dianjisoiusuo)

        WebUIAssert.asserts_url(
            "https://sgzzlb.lingxigames.com/news/search/?keyword=%E4%B8%89%E5%9B%BD%E5%BF%97%E6%88%98%E7%95%A5%E7%89%88",
            base.base_get_current_url())
        base.base_move_to_element(wx_icon)
        base.base_move_to_element(wx_gzh)
        print(base.base_get_element_text(wx_gzh))
        WebUIAssert.assert_text(get_quit_driver, "微信公众号", base.base_get_element_text(wx_gzh))
        # allure.attach.file((GetFilePath().get_all_image_path(r'image/')),
        #                    attachment_type=allure.attachment_type.PNG, name='错误截图')
        # allure.attach(body='测试测试', name='测试附件名字', attachment_type=allure.attachment_type.TEXT)

        # base.base_move_to_element(wb_icon)
        # WebUIAssert.asserts(True, base.base_element_if_selected(wb_icon))
        # base.base_move_to_element(qq_icon)

        # base.base_click(xinwenzixun)
        # base.base_switch_to_new_handle()
        # base.base_switch_to_current_handle()
        # base.base_click(saijizhuanti)
        # base.base_switch_to_new_handle()
        # base.base_switch_to_current_handle()
        # base.base_click(shitingzhan)
        # base.base_switch_to_new_handle()
        # base.base_switch_to_current_handle()
        # base.base_click(ziliaoku)
        # base.base_switch_to_new_handle()
        # base.base_switch_to_current_handle()
        # base.base_click(guanwangluntan)
        # base.base_switch_to_new_handle()
        # base.base_switch_to_current_handle()
