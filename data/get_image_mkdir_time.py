# -*-coding = utf-8 -*-
'''
@File    :  get_image_mkdir_time.py
@Time    :  2023/4/15 22:32
@Author  :  yangjingkang(靖康阳)
@Gitee   :  https://gitee.com/jingkangyang
@Jianshu :  靖康阳
@Contact :  1097904758@qq.com
@License :  (C)Copyright 2022--2025, Micro-Circle
@Software:  PyCharm
@Desc    :  get_image_mkdir_time
'''
import os
from datetime import datetime

from data.get_filepath import GetFilePath
#
# ctime = os.path.getctime("2023_04_15 21_28_15.png")  # 创建时间
# ctime_string = datetime.fromtimestamp(int(ctime))
#
# ctime2 = os.path.getctime("2023_04_15 22_22_56.png")  # 创建时间
# ctime_string2 = datetime.fromtimestamp(int(ctime2))
# ctime3 = os.path.getctime("2023_04_16 22_22_56.png")  # 创建时间
# ctime_string3 = datetime.fromtimestamp(int(ctime3))
# print(
#     f"创建时间：{ctime_string}",
#     f"创建时间：{ctime_string2}",
# f"创建时间：{ctime_string2}"
# )
#
# print(os.listdir("../image"))

# for files in os.walk("../image"):
#     print(files[-1])
#     image_file = files[-1][-1]
#     print(image_file)
#     print(files[-1][-1])
#     print(type(image_file))
#     print(os.path.abspath(image_file))
# import os
#
# dir_name = GetFilePath().get_all_file_path(r"image")
# print(dir_name)
# file_list = os.listdir(dir_name)
# # 获取按照文件时间创建排序的列表，默认是按时间升序
# new_file_list = sorted(file_list, key=lambda file: os.path.getctime(os.path.join(dir_name, file)))
# print(new_file_list[-1])

import shutil
import os
from pathlib import Path


# 第一种：删除一个文件夹，无论里面是否有文件或文件夹
# (不支持文件，文件夹不存在会报错)
from loging.log import log


def del_files0(dir_path):
    shutil.rmtree(dir_path)


# 第二种 递归删除dir_path目标文件夹下所有文件，以及各级子文件夹下文件，保留各级空文件夹
# (支持文件，文件夹不存在不报错)
def del_files(dir_path):
    if os.path.isfile(dir_path):
        try:
            os.remove(dir_path)  # 这个可以删除单个文件，不能删除文件夹
        except BaseException as e:
            print(e)
    elif os.path.isdir(dir_path):
        file_lis = os.listdir(dir_path)
        for file_name in file_lis:
            # if file_name != 'wibot.log':
            tf = os.path.join(dir_path, file_name)
            del_files(tf)
    print('ok')


def del_image_file(dir_path):
    for root, dirs, files in os.walk(dir_path, topdown=False):
        # 第一步：删除文件
        for name in files:
            os.remove(os.path.join(root, name))  # 删除文件
        # 第二步：删除空文件夹
        for name in dirs:
            os.rmdir(os.path.join(root, name))  # 删除一个空目录
    log.info(f"初始化{dir_path}文件夹成功")

if __name__ == '__main__':
    del_image_file('../image1')

