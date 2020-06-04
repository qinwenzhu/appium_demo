# -*- coding:utf-8 -*-
# @Time: 2020/3/18 18:10
# @Author: wenqin_zhu
# @File: handle_config.py
# @Software: PyCharm


"""
对yaml格式的配置文件的操作
"""

import yaml
import env
from vendor.config.config_handle import ConfigHandle


class YamlHandle(ConfigHandle):
    def __init__(self, dir_name, file_name):                    # 知识点
        """
        @param dir_name: 文件夹名字,从env.py文件导入，eg:env.ELEMENTINI_PATH
        @param file_name: 文件名字
        """
        print(file_name)
        try:
            self.f = open(super().get_file_full_path_name(dir_name, file_name), 'r', encoding='utf-8')
            self.cfg = self.f.read()
        except:
            print("配置文件不存在")

    """
        获取yaml文件中的字典value值，可获取字典值任意一层
        ele_dict = {
            'password_input':
                {
                'dec': '登录按钮', 
                'type': 'XPATH', 
                'value': '//button'
                },
            'account_number_input':
                {
                'dec': '账号输入框', 
                'type': 'CLASS_NAME', 
                'value': 'ivu-input', 
                'index': 0
                },
        }
    """
    def get_value(self, *keys):
        """
        @param keys:yaml文件中的key值，可多层，['password_input','dec']或者['password_input']
        @return: 返回字典中value值
        """
        try:
            ele_dict = yaml.load(self.cfg, Loader=yaml.FullLoader)  # 用load方法转字典
            print(ele_dict)
            if not keys:
                return ele_dict
            else:
                for key in keys:
                    tmp = ele_dict.get(key)
                    if tmp is not None:
                        ele_dict = tmp
                return ele_dict
        except:
            print("值不存在")

    def __del__(self):
        try:
            self.f.close()
        except:
            print("文件操作符关闭失败")


if __name__ == '__main__':
    yh = YamlHandle(env.ELEMENTINI_PATH, 'admin_login.yaml')
    print(yh.get_value('login_button'))


# import yaml
# import os
#
#
# class HandleConfig(object):
#     """  读取配置文件 """
#
#     def __init__(self, file_name):
#         self.config = self.load_config(file_name)
#
#     def load_config(self, file_name):
#         if os.path.exists(file_name):
#             with open(file_name, mode='r', encoding='utf-8') as file:
#                 configs = yaml.safe_load(file)
#         else:
#             with open(file_name, mode='w', encoding='utf-8') as file:
#                 configs = yaml.safe_load(file)
#
#         # with open(path_to_config) as file:
#         #     try:
#         #         con_file = yaml.safe_load(file)
#         #     except Exception as e:
#         #         print("文件未找到！")
#         #         raise
#         return configs
#
#
# if __name__ == '__main__':
#     pass
