from turtle import *

speed(0)

for x in range(7):
  color('red')
  begin_fill()
  forward(200)
  right(90)
  forward(10)
  right(90)
  forward(200)
  end_fill()
  right(180)
  color('white')
  begin_fill()
  forward(200)
  right(90)
  forward(10)
  right(90)
  forward(200)
  end_fill()
  right(180)
  
goto(0,0)

color('navyblue')
begin_fill()
forward(100)
right(90)
forward(80)
right(90)
forward(100)
end_fill()

goto(35,-13)

color('yellow')
begin_fill()
circle(25)
end_fill()

goto(45,-12)

color('navyblue')
begin_fill()
circle(25)
end_fill()

goto(80,-50)

color('yellow')
begin_fill()
for x in range(14):
  right(-120+13)
  forward(10)
  right(120+13)
  forward(10)
end_fill()
