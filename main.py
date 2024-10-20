from turtle import *
from random import *
import turtle
import time

# Screen Setup;
setup(800, 500)
title("Turtle Race - Ajay Saini")
bgcolor("green")
speed(0)

# Heading title;
penup()
goto(-100, 205)
color("red")
write("Who will win?!", font=("Arial", 20, "bold"))

#Ground (Middle brown part);
goto(-350, 200)
penup()
color("chocolate")
begin_fill()

for i in range(2):
  forward(700)
  right(90)
  forward(400)
  right(90)
end_fill()

# Finishline;
gap_size = 20
shape("square")
penup()

# White Square Row 1;
color("white")
for i in range(10):
  goto(250, (170 - (i * gap_size * 2)))
  stamp()

# White Square Row 2;

for i in range(10):
  goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
  stamp()

# Black Square Row 1;
color("black")
for i in range(10):
  goto(250, (190 - (i * gap_size * 2)))
  stamp()

for i in range(10):
  goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
  stamp()
#Turtle Names
n=input("Enter your name: ")
n2=input("Enter your name: ")
n3=input("Enter your name: ")

# Blue Turtle;
blue_turtle = Turtle()
blue_turtle.color("pink")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300,150)
blue_turtle.write(n, font=("Arial", 20, "bold"))
blue_turtle.pendown()

# Pink Turtle;
pink_turtle = Turtle()
pink_turtle.color("cyan")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300,50)
pink_turtle.write(n2, font=("Arial", 20, "bold"))
pink_turtle.pendown()

#  Green Turtle;
green_turtle = Turtle()
green_turtle.color("light green")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300,-100)
green_turtle.write(n3, font=("Arial", 20, "bold"))
green_turtle.pendown()

# Do not move for one second at the start of the race;
time.sleep(1)

#move the Turtle;

while blue_turtle.xcor()<=230 and blue_turtle.xcor()<=230:
  blue_turtle.forward(randint(1,10))
  pink_turtle.forward(randint(1,10))
  green_turtle.forward(randint(1,10))

# Celebration;
if blue_turtle.xcor()<pink_turtle.xcor():
   print("Bravo! Good job",n,"!")
   for i in range(72):
     pink_turtle.right(90)
elif blue_turtle.xcor()<pink_turtle.xcor():
   print("Wow! Good job",n2,"!")
   for i in range(72):
    blue_turtle.right(90)
else:
  print("Hurray! Good Job",n3,"!")
  for i in range(72):
    green_turtle.right(90)