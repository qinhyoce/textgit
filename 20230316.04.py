"""
保留小数的方法
"""
print("=============分界线===============")
import math
print(math.pi)
#1·使用字符串格式化
print("%.3f"%math.pi)
print("=============分界线===============")
#2`使用decimal模块
from decimal import Decimal

print(Decimal(math.pi).quantize(Decimal("0.00000")))
#3.使用round（）函数 不精确
print(round(math.pi,3))# 前田数字，后填保留到的位次

#5·使用re模块
import re
print(re.findall(r"\d{1,}?\.\d{2}",str(math.pi)))
#4·使用序列切片
print(str(math.pi).split('.')[0]+'.'+str(math.pi).split(',')[1][2])#搞不懂先不管
