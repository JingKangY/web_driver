# -*-coding = utf-8 -*-
'''
@File    :  page_elements.py
@Time    :  2023/4/8 20:37
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  元素
'''
from selenium.webdriver.common.by import By

url = "https://www.baidu.com"
lingxi_url = "https://sgzzlb.lingxigames.com/website/"
click_test = By.CSS_SELECTOR, '#kw'
login_btn = By.XPATH, "//a[@id='s-top-loginbtn']"
username_input = By.CSS_SELECTOR, "#TANGRAM__PSP_11__userName"
password_input = By.CSS_SELECTOR, "#TANGRAM__PSP_11__password"
login = By.CSS_SELECTOR, "#TANGRAM__PSP_11__submit"
move_button = By.CLASS_NAME, "user-name c-font-normal c-color-t"
login_out = By.LINK_TEXT, "退出登录"

xinwenzixun = By.XPATH, "//a[contains(text(),'新闻资讯')]"
saijizhuanti = By.XPATH, "//a[contains(text(),'赛季专题')]"
shitingzhan = By.XPATH, "//a[contains(text(),'视听站')]"
ziliaoku = By.XPATH, "//a[contains(text(),'资料库')]"
guanwangluntan = By.XPATH, "//a[contains(text(),'官网论坛')]"
wx_icon = By.CLASS_NAME, "icon-wx"
wb_icon = By.CLASS_NAME, "icon-wb"
qq_icon = By.CLASS_NAME, "icon-qq"

sousuoshurukuang = By.CLASS_NAME, "keywords"
dianjisoiusuo = By.XPATH, "//a[contains(text(),'点击搜索')]"
wx_gzh = By.XPATH, "//h4[contains(text(),'微信公众号')]"