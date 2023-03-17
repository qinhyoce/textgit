from turtle import *
pencolor("red")
pensize(4)
def fib(n):
    if n<2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(13):
    circle(fib(i),90)


    
