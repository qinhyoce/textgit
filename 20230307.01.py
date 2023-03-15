from turtle import *
pensize(2)
speed(10)
c=["green","purple","orange","red"]
for i in range(10):
    penup()
    pencolor(c[i%4])
    goto(0,-15*i)
    pendown()
    circle(15+i*15)
    
