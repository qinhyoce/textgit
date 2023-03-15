import random
strl=input("你的名字：")
print("hello!{}".format(strl))
guard=ord(strl[0])%100
print("你的幸运数字是：",random.choice(range(guard)))
