'''
Description: 
Author: Huang Wen
Date: 2022-04-12 15:37:13
LastEditTime: 2022-04-24 16:12:55
LastEditors: Huang Wen
'''
import hashlib


# md5加密方法
def gen_md5(_str):
    hl = hashlib.md5()
    hl.update(_str.encode(encoding='utf-8'))
    return hl.hexdigest()
