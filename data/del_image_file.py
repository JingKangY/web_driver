# -*-coding = utf-8 -*-
'''
@File    :  del_image_file.py
@Time    :  2023/4/16 14:20
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  del_image_file
'''
import os

from data.get_filepath import GetFilePath
from loging.log import log


class DelImageFile(object):

    def del_image_file(self, dir_path):
        image_file = os.path.exists(dir_path)
        if image_file == True:
            for root, dirs, files in os.walk(dir_path, topdown=False):
                # 第一步：删除文件
                for name in files:
                    os.remove(os.path.join(root, name))  # 删除文件
                # 第二步：删除空文件夹
                for name in dirs:
                    os.rmdir(os.path.join(root, name))  # 删除一个空目录
            log.info(f"初始化{dir_path}文件夹成功")
        else:
            log.error(f'文件夹{dir_path}不存在，请重新输入')


if __name__ == '__main__':
    DelImageFile().del_image_file(GetFilePath().get_all_file_path(r'image2/'))
