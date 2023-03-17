#python learning
#第一节 输出函数和输入函数
n=input("请输入你的名字")
print("你的名字是：",n)
#第二节 转义符\
print("这世界从来都不美好")
print("这世界\n从来都不美好")#换行
print("这世界\r从来都不美好")#后覆盖前
print("这世界\b从来都不美好")#删除前一个字符
print("这世界\t从来都不美好")#制表符，补齐四个空格
print("这世界\\从来都不美好")#输出\
print(R"这世界\\从来\n都\r不美好")#r/R,将转义符无效化
print("这世界从来都\"不美好\"")#无效化""
#第三节 关键字
import keyword
print(keyword.kwlist)