from turtle import *

#we want to paint a house

#step 1: draw a squer
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of squer

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)       #height og the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
right(150)
forward(200)
left(120)
forward(200)

penup()
goto(150,150)
pendown()

left(30)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)

forward(30)
penup()
forward(130)
pendown()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)










exitonclick()