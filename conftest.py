# -*-coding = utf-8 -*-
'''
@File    :  conftest.py
@Time    :  2023/4/9 21:36
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  conftest
'''
from common.get_driver import GetDriver
import pytest
from common import page_elements
from data.del_image_file import DelImageFile
from data.get_filepath import GetFilePath


# 前置回去driver 后置关闭driver
@pytest.fixture(scope="class")
def get_quit_driver():
    get_driver = GetDriver().get_driver(page_elements.lingxi_url, 'Chrome')
    yield get_driver
    quit_driver = GetDriver().quit_driver()
    return quit_driver


# 初始化所有截图
@pytest.fixture(scope="class")
def del_image_png():
    DelImageFile().del_image_file(GetFilePath().get_all_file_path(r'image/'))
