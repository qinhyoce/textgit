"""
python learing
第一节 数字类型
可通过type()函数查看数据类型
"""
"""
1·整数类型（int）
十进制：
二进制：0B1011
八进制：0O3427
十六进制：0XAD5

"""
x = 0O37
y = 0B10011
print(x,y)
print(type(x))
"""
2`浮点数型（float） 指有小数的数据类型
可用科学计数法表示
"""
a = 1.02
print(type(a))
b = 314159267E-8
print(b)
"""
3·复数类型（complex） 由实数和虚数组成
表示为a+bJ 其中a、b都是浮点型
"""
n=12+0.3J
print(type(n))
print(n.real)#返回实数部分
print(n.imag)#返回虚数部分
"""
布尔型（bool） Ture=1 False=0
"""
f=eval(input("输入第一个数字"))
j=eval(input("输入第二个数字"))
print(j>f)
print(j<f)
print(j!=f)
print(j==f)
print(j>=f)
print(j<=f)
F=j<=f and j==f
J=j!=f or f<j
print(J and F)
print(J or F)
print(not J)
"""
第二节 数字类型的运算符
"""
g=eval(input("第一个未知数"))
h=eval(input("第二个未知数"))
print(g+h)
print(g-h)
print(g*h)
print(g/h)
print(g//h)#整除运算
print(g**h)
print(g%h)#模运算 等价于 g-(g//h)*h
"""
第三节 保留小数
"""
