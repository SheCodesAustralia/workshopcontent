#Turtle Graphics Game
import turtle


#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("Navy")

#Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("darkorange")
player.shape("turtle")
player.penup()
player.speed(0) 

#Set speed variable
speed = 1

#Define  functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def inscreasespeed():
    global speed
    speed += 1

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(inscreasespeed, "Up") 




while True:
    
    player.forward(speed)

    #Boundary Checking x cordinate
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
    #Boundary Checking x cordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)













delay = raw_input("Press Enter to finish.")

