#Turtle Graphics Game
import turtle
import math
import random
import os
import time

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("kbgame-bg.gif")
wn.tracer(3)


#Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
mypen.setposition(0, 0)



#Create player turtle
player = turtle.Turtle()
player.color("darkorange")
player.shape("turtle")
player.penup()
player.speed(0)

#Create compition turtle
comp = turtle.Turtle()
comp.color("red")
comp.shape("turtle")
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

#Create Comp score
mypen2 = turtle.Turtle()
mypen2.color("red")
mypen2.hideturtle()


#Create variabl score
score = 0
compscore = 0

#create food
maxFoods = 10
foods = []

for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.color("lightgreen")
    new_food.shape("circle")
    new_food.shapesize(.5)
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)

#Set speed variable
speed = 1


#Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10*6

#Define  functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def inscreasespeed():
    global speed
    speed += 1

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(inscreasespeed, "Up")


while True:
    gametime = 0
    if gametime == 6 or time.time() > timeout:
        break
    gametime = gametime - 1

    player.forward(speed)
    comp.forward(12)

    #Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    #Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    #Boundary Comp Checking x coordinate
    if comp.xcor() > 280 or comp.xcor() <-280:
        comp.right(random.randint(30,90))
        os.system("afplay bounce.mp3&")

    #Boundary Comp Checking y coordinate
    if comp.ycor() > 280 or comp.ycor() <-280:
        comp.right(random.randint(30,90))
        os.system("afplay bounce.mp3&")
        

    #Move Food around
    for food in foods:
        food.forward(3)

        #Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() <-290:
           food.right(180)
           os.system("afplay bounce.mp3&")

        #Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() <-290:
           food.right(180)
           os.system("afplay bounce.mp3&")

        #Player Collision checking
        if isCollision(player, food):
           food.setposition(random.randint(-290, 290), random.randint(-290, 290))
           food.right(random.randint(0,360))
           os.system("afplay chomp.mp3&")
           score+=1
           #Draw the score on the screen
           mypen.undo()
           mypen.penup()
           mypen.hideturtle()
           mypen.setposition(-290, 310)
           scorestring ="Score: %s" %score
           mypen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

       # Comp Collision checking
        if isCollision(comp, food):
           food.setposition(random.randint(-290, 290), random.randint(-290, 290))
           food.right(random.randint(0,360))
           os.system("afplay chomp.mp3&")
           compscore+=1
           #Draw the Comp score on the screen
           mypen2.undo()
           mypen2.penup()
           mypen2.hideturtle()
           mypen2.setposition(200, 310)
           scorestring ="Score: %s" %compscore
           mypen2.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


if (int(score) > int(compscore)):
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You LOOSE", False, align="center", font=("Arial", 28, "normal"))












# delay = raw_input("Press Enter to finish.")
