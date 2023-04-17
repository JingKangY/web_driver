import allure

from common.base import Base
from data.get_filepath import GetFilePath
from loging.log import *
import sys,os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)


class WebUIAssert:
    '''
    断言封装
    '''

    @allure.step("step：断言页面URL是否一致")
    def asserts_url(self, expect, res_actual):  # 比对断言结果，参数：expect，actual 结果：断言是否通过
        '''
        :param expect: 预期结果
        :param res_actual: 实际结果
        :return: 用例是否通过
        '''
        try:
            log.debug(f'URL实际结果为：{res_actual}')
            log.debug(f'URL预期结果为：{expect}')
            assert str(res_actual) == str(expect)  # 成立返回TURE，失败返回FALSE
            log.info('断言用例通过！')
        except AssertionError as e:
            log.error(f'断言失败，URL实际结果为：{res_actual}，URL预期结果为：{expect}')
            log.error(f'断言用例不通过！')
            raise e

    @allure.step("step：响应状态码结果断言")
    def assert_text(self, driver,expect_code, actual_code):
        try:
            log.debug(f'URL实际结果为：{actual_code}')
            log.debug(f'URL预期结果为：{expect_code}')
            assert str(actual_code) == str(expect_code)  # 成立返回TURE，失败返回FALSE
            log.info('断言Code用例通过！')
        except AssertionError as e:
            Base(driver).base_get_image()
            # 断言失败添加图片
            allure.attach.file((GetFilePath().get_all_image_path(r'image/')),
                               attachment_type=allure.attachment_type.PNG, name='错误截图')
            #allure.attach(body='测试测试', name='测试附件名字', attachment_type=allure.attachment_type.TEXT)
            log.error(f'断言失败，URL实际结果为：{actual_code}，Response预期结果为：{expect_code}')
            log.error('断言用例不通过！')
            raise e

    @allure.step("step：响应文本信息结果断言")
    def assert_message(self, expect_mes, actual_mes):
        try:
            log.debug(f'Response_Message实际结果为：{actual_mes}')
            log.debug(f'Response_Message预期结果为：{expect_mes}')
            assert str(actual_mes) == str(expect_mes)  # 成立返回TURE，失败返回FALSE
            log.info('断言Message用例通过！')
        except AssertionError as e:
            log.error(f'断言失败，Response_Message实际结果为：{actual_mes}，Response预期结果为：{expect_mes}')
            log.error('断言用例不通过！')
            raise e

    @allure.step("step：断言是否一致")
    def asserts(self, expect, res_actual):  # 比对断言结果，参数：expect，actual 结果：断言是否通过
        '''
        :param expect: 预期结果
        :param res_actual: 实际结果
        :return: 用例是否通过
        '''
        try:
            log.debug(f'实际结果为：{res_actual}')
            log.debug(f'预期结果为：{expect}')
            assert str(res_actual) == str(expect)  # 成立返回TURE，失败返回FALSE
            log.info('断言用例通过！')
        except AssertionError as e:
            log.error(f'断言失败，实际结果为：{res_actual}，预期结果为：{expect}')
            log.error(f'断言用例不通过！')
            raise e


WebUIAssert = WebUIAssert()
