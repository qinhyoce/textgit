"""
第五节 字符串的常用方法
"""
# 1·查找元素位置(find) 找不到返回-1
s1="月亮小姐会哭么？\n拜托了！骑士先生\n你的颜色留在这里了呢\n唔，禁忌知识..."
print(s1)
print(s1.find("月")) # 理论上讲会输出第一次出现处的下标
s2="i am sorry to tell you that you are have already defeat"
print(s2.find("m"))
s3 = "pythonlearning"
print(s3.find("o",2,7)) # h后两位用于截取字符串
s4= "dabuzhaoo"
print(s4.find("a"))
s5="打不着哦，我的心意要好好的收下哦"
print(s5.find("我"))
print("============分割线==============")
# 2`统计字符串片段(count) 找不到返回0
print(s1.count("月"))
# 3·替换指定字符串片段(replace) 第一个为要替换的字符，第二个为用于替换的字符，第三个指次数
print(s2.replace("defeat","seccus")) # 不写替换次数默认所有/写了就由前往后
# 4·大小写转换（upper/lower）
S3=s3.upper()
print(S3)
print(S3.lower())
print("============分割线==============")
# 5·指定分割点对字符串进行分割（split） 分割点，分割次数
print(s4.split("a"))# 分割后获得一个列表
print(s4.split("a",1))
# 6·去除字符段的首尾z字符（strip）
s6="     woww     "
s7=s6.strip()
print(s6.strip())# 不写默认为空格
print(s6.replace(" ",""))
print(s7.strip("w"))
print("============分割线==============")

