# 导包
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from common.asserts import WebUIAssert
from common.page_elements import *
from common.base import *

# 实例化浏览器
driver = webdriver.Chrome()
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 打开网址
driver.get('https://sgzzlb.lingxigames.com/website/')
# # allure.attach(body='测试测试', name='测试附件名字', attachment_type=allure.attachment_type.TEXT)
base = Base(driver)
# base.base_click(xinwenzixun)
# sleep(3)
# base.base_forward_or_back(forward_or_back='back')
# sleep(3)
# base.base_forward_or_back(forward_or_back='forward')
# sleep(2)
base.base_input(sousuoshurukuang, "三国志战略版")
sleep(2)
base.base_send_keys(sousuoshurukuang,'ENTER')
# base.base_click(sousuoshurukuang)
# base.base_right_or_double_click(sousuoshurukuang,'double')
sleep(2)
#
# base.base_right_or_double_click(sousuoshurukuang,'right')
# sleep(2)
# base.base_click(sousuoshurukuang)
# sleep(2)


# base.base_send_keys(sousuoshurukuang, 'a')
# sleep(3)
# base.base_send_keys(sousuoshurukuang, 'c')
# base.base_delete(sousuoshurukuang)
# base.base_send_keys(sousuoshurukuang, 'v')
# sleep(3)
# base.base_click(dianjisoiusuo)
# sleep(2)

# base.base_move_to_element(wb_icon)
# base.base_get_image()
# WebUIAssert.asserts(True, base.base_element_if_selected(wb_icon))
# print(base.base_get_element_text(xinwenzixun))
# base.base_switch_to_new_handle()
#
# print(base.base_get_current_url())
# EC.title_is("三国志・战略版")
# base.base_switch_to_current_handle()
# base.base_click(saijizhuanti)
# print(base.base_get_element_text(saijizhuanti))
#
# base.base_switch_to_new_handle()
# print(base.base_get_current_url())
# base.base_switch_to_current_handle()
#
# sleep(3)

# 关闭页面
driver.quit()
