# @Date    : 2022/6/18
# @Author  : Jin Chun Long (chunlong.jin@westwell-lab.com)
# @Project : abort_vehicle
# @File : AbortVehicle.py
# @Software: PyCharm

import json


# 获取配置文件中对应配置
def get_conf(arg1,arg2):
    with open('ww/myutil/my.conf', 'r', encoding='utf-8') as config_file:
        confStr = config_file.read()
    conf = json.JSONDecoder().decode(confStr)
    mysqlRes = conf[arg1][arg2]
    return mysqlRes
