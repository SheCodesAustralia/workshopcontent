+++
title = "More cabbage, more!"
date = 2021-02-04T18:39:00+08:00
weight = 70
chapter = true
pre = "<b>7. </b>"
+++

### Part 7

# More cabbage, more!

In this section you are going to develop a way of having multiple space
 cabbages \(food\) moving around the screen for your turtle to chomp.
 You are going to do this using the python functions of Lists and Loops

Step 1.  First we create the maximum number of cabbages and an empty list by
 editing the `\# Create food section` with the following code at the top:

```python
# Create food
maxFoods = 6
foods = []
```

Step 2.  Next you create a for loop using maxFoods as the range updating the code

From this:

```python
food = turtle.Turtle()
food.color("lightgreen")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(random.randint(-290, 290), random.randint(-290, 290))
```

To this:

```python
for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.color("lightgreen")
    new_food.shape("circle")
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)
```

So we use the append function to add our maximum number of cabbages held in the
 list, so foods.\[1\] is a turtle object, foods.\[2\] is a turtle object etc. etc.

Step 3.  Now you need to do the same thing for moving the turtle within the
 \# Move Food around section by changing

this:

```python
# Move food around
    food.forward(3)
```

to:

```python
# Move food around
    for food in foods:
        food.forward(3)
```

And then indent and change

this:

```python
    # Boundary Food Checking x coordinate
    if food.xcor() > 290 or food.xcor() <- 290:
        food.right(180)

    # Boundary Food Checking y coordinate
    if food.ycor() > 290 or food.ycor() <- 290:
        food.right(180)
```

to:

```python
        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() <- 290:
            food.right(180)

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() <- 290:
            food.right(180)
```

Step 4.  Now let’s move \(cut and paste\) your food collision checking code
 within move goal loop. Make sure you indent your code now looks like:

```python
    #Move food around
    for food in foods:
        food.forward(3)

       #Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() <-290:
           food.right(180)

        #Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() <-290:
           food.right(180)

        # Collision checking
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
```

Step 5.  Save the game as kbgame7 and run your module

You now have multiple cabbages moving around your screen however the screen can
 start to look a bit jumpy, to fix this we can add the tracer function to the
 program.
 This tells the computer not to refresh the screen each time and speeds up the
 animation.

Step 6.  Add the tracer function by typing the following at the end of the
 \#Set up screen area:

```python
wn.tracer(3)
```

Step 7.  Save and run your module

You can play with your code by increasing the maxFood number

Your code should now look like this: [kbgame7.py](/python_game/src/kbgame7.py)

**Congratulations Module 7 Completed**
