from turtle import *
from random import *
print("我要对你开大啦！")

def star (x,y):
    penup()
    goto(x,y)
    pencolor('light yellow')
    fillcolor('light yellow')
    pendown()
    begin_fill()
    for x in range(8):
        if x % 2 == 0:
            left(30)
        else:
            right(120)
        fd(10)
    end_fill()

def f (x,y):
    penup()
    goto(x,y)
    pencolor('yellow')
    fillcolor('light yellow')
    pendown()
    begin_fill()
    for x in range(8):
        if x % 2 == 0:
            left(30)
        else:
            right(120)
        fd(8)
    end_fill()

# 画脸
speed(0)
pensize(5)
right(90)
penup()
fd(100)
left(90)
pendown()
begin_fill()
pencolor("#B26A0F")  # head side color
circle(150)
fillcolor("#F9E549")  # face color
end_fill()

#绿色花瓣
penup()
goto(-95,161)
right(250)
pendown()

pencolor("green")
fillcolor('light green')
begin_fill()
circle(60,90)
circle(120,75)
circle(60,120)
penup()
goto(-115,141)
pendown()
right(165)
circle(150,48)
end_fill()

#红色花瓣
pencolor('red')
fillcolor('pink')
begin_fill()
right(110)
circle(50,90)
circle(100,75)
circle(90,85)
right (73)
circle(150,-63)
end_fill()

#粉色花瓣
penup()
goto(-35,-100)
pendown()
pencolor('orange')
fillcolor("#FF6F91")
begin_fill()
right(50)
circle(50,85)
circle(100,90)
circle(60,105)
right(115)
circle(150,-50)
end_fill()

#紫色花瓣
penup()
pencolor('purple')
fillcolor( '#DCA6DC')
begin_fill()
goto(100,-70)
pendown()
right(50)
circle(60,95)
circle(150,90)
circle(60,107)
right(111)
circle(150,-80)
end_fill()

#蓝色花瓣
penup()
pencolor('#1E90FF')
fillcolor('light blue')
goto(140,120)
pendown()
begin_fill()
circle(90,100)
circle(190,60)
circle(90,100)
right(79)
circle(150,-100)
end_fill()

#内部再画一遍
penup()
goto(-33,-94)
right(133)
pendown()
pencolor("#B26A0F")  # head side color
fillcolor("#F9E549")  # face color
begin_fill()
circle(150)
end_fill()

#内部细节
#眼睛
#外部细节
#眼睛1
penup()
goto (-10,140)
pendown()
left(120)
fillcolor('white')
begin_fill()
circle(40,120)
right(10)
circle(100,40)
left(10)
circle(40,120)
circle(90,60)
end_fill()

penup()
goto (-13,118)
pencolor('grey')
fillcolor('black')
begin_fill()
pendown()
circle(39)
end_fill()

penup()
goto(-16,130)
pencolor('grey')
fillcolor('white')
begin_fill()
pendown()
circle(18)
end_fill()

#另一只眼睛
penup()
goto (120,100)
pencolor("#B26A0F")
fillcolor('white')
pendown()
begin_fill()
left(20)
circle(40,120)
left(10)
circle(100,50)
left(10)
circle(40,100)
left(16)
circle(100,58)
end_fill()

penup()
goto(80,120)
pendown()
left(68)
pencolor('grey')
fillcolor('black')
begin_fill()
circle(39)
end_fill()
fillcolor('white')
begin_fill()
circle(18)
end_fill()

#嘴巴
penup()
goto(10,35)
pendown()
pencolor()
pencolor('red')
fillcolor('coral')
right(30)
begin_fill()
circle(100,30)
left(60)
circle(80,40)
left(40)
circle(50,40)
left(40)
circle(80,43)
end_fill()

right(20)
pencolor('white')
fillcolor('white')
begin_fill()
circle(25,-150)
right(90)
pensize(1)
circle(80,-32)
end_fill()

penup()
goto(10,35)
pendown()
pencolor('firebrick')
pensize(5)
circle(100,30)
left(60)
circle(80,40)
left(40)
circle(50,40)
left(40)
circle(80,43)

#大星星
star(-100,120)
star(100,100)
star(120,60)

#小星星~
for i in range (10):
    f(randint(-400,400),randint(-400,400))

done()
