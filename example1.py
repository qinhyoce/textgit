#print("hello0 woorld!")
#a=3
#print("数字式：",a)
#b=5
#print(a>b)
#print(a!=b)
#n=19234E-3
#print("%.2f"%n)
#import math
#import decimal
#print(decimal(math.pi).quantize(decimal("0.00")))
#1·查找元素位置(find)
s1="月亮小姐会哭么？\n拜托了！骑士先生\n你的颜色留在这里了呢\n唔，禁忌知识..."
print(s1)
print=(s1.find("月"))#理论上讲会输出第一次出现处的下标
s2="i am sorry to tell you that you are have already defeat"
print(s2.find("m"))
s3 = "pythonlearning"
print(s3.find("o",2,7))#h后两位用于截取字符串
#2`统计字符串片段(count)
print(s1.count("月"))