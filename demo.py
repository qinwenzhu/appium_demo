# -*- coding:utf-8 -*-
# @Time: 2020/6/4 15:59
# @Author: wenqin_zhu
# @File: demo.py
# @Software: PyCharm

import yaml


class YamlPackage:

    def __init__(self, path_to_yaml):
        self.get_data = self.read_config_by_yaml(path_to_yaml)

    def read_config_by_yaml(self, path_to_yaml):
        """
        读取yaml格式的配置文件
        :param path_to_yaml:
        :return: 返回成功读取后的数据
        """
        with open(file=path_to_yaml, mode="r", encoding="utf-8") as file:
            try:
                parsed_data = yaml.safe_load(file)
            except Exception as e:
                print(f"文件读取失败！当前读取的文件路径为：{path_to_yaml}")
                raise e
        print(f"读取yaml格式的文件数据为：{parsed_data}")
        return parsed_data


if __name__ == '__main__':

    data = YamlPackage("demo.yaml").get_data
    print(data)

    # TODO 文件操作扩展
    # # python 对文件进行读写操作
    # # TODO 读取文件    r 只读   r+ w+ a+ 读写
    # file = open(file="demo.yaml", mode="r", encoding="utf-8")      # 打开文件
    #
    # # 读取文件 文件读取一行 少一行，以下函数需单个测试调用
    # text1 = file.read()          # 读取字节到字符串中    原样输出源文件
    # print(f"类型：{type(file.read())}")
    # print(f"读取的数据为：{text1}")
    #
    # # text2 = file.readline()      # 一次读取一行，包括换行符
    # # print(f"类型：{type(file.readline())}, 读取的数据为：{text2}")
    #
    # # text3 = file.readlines()     # 一次性读取整个文件，返回类型为 列表 list
    # # print(f"类型：{type(file.readlines())}, 读取的数据为：{text3}")
    #
    # file.close()      # 关闭文件
    #
    # print("-----------------------------------------------------------------------------")
    #
    # file = open(file="demo.yaml", mode="a+", encoding="utf-8")  # 打开文件
    # # TODO 写入/追加文件    r 只读   r+ w+ a+ 读写
    # file.write("\nadd new content!")
    # file.close()  # 关闭文件
    #
    # file = open(file="demo.yaml", mode="r", encoding="utf-8")  # 打开文件
    # # TODO 写入/追加文件    r 只读   r+ w+ a+ 读写
    # print(file.readlines())
    # file.close()  # 关闭文件
