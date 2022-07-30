+++
title = "What's the turtle chomping?"
date = 2021-01-25T14:55:24+08:00
weight = 40
chapter = true
pre = "<b>4. </b>"
+++

### Part 4

# What's the turtle chomping?

OK so now you have your turtle that we can move around the screen and if we
 bump into any of the borders your turtle will bounce off at 180&deg;.
 Now we need an objective for the game, something for your turtle to do and to
 score points for doing. For this game you are going to have your turtle chase
 and chomp space cabbages (because we are making a green circle object for
 your turtle to chase). You could choose a different colour and shape such as
 space cheese (e.g. yellow triangle).

Step 1.  Create the goal / objective, type the following under a
 `# Create food` section after `player.speed(0)`

```python

# Create food
food = turtle.Turtle()
food.color("lightgreen")
food.shape("circle")
food.penup()
food.speed(0)
```

Step 2.  Save the game as kbgame4.py and then run the module.

{{% notice note %}}
you should see the light green circle on the screen and can move around it
{{% /notice %}}

Step 3.  Now we are going to set the cabbage in a position by typing the
 following after food.speed(0):

```python
food.setposition(-100, 100) 
```

Step 4.  Save and run module kbgame4

Step 5.  Next we need to add collision detection as this will allow us to
 calculate when your turtle collides with (chomps) the space cabbage.
 We do this by using a bit of math to work out where the turtle and cabbage is
 and if they are touching or the distance between them is small. For the math
 nerds here we will use one of Pythagoras theories. To do that we need to
 import the math libraries at the top of our application after import turtle:

```python
# Turtle Graphics Game – Space Turtle Chomp
import turtle
import math
```

Step 6.  Now we write the math formula that will take the x coordinate of the
 turtle subtracting from the x coordinate of the cabbage then squaring it and
 doing the same for the y coordinates for the turtle and cabbage then working
 out the square root. It’s OK not to completely understand
 (I’m not sure I do 😄)
 but you need to type the following at the end of your While Loop:

```python
  

    # Collision checking
    d = math.sqrt(math.pow(player.xcor() - food.xcor(), 2) + math.pow(player.ycor() - food.ycor(),2))
    if d < 20:
        food.hideturtle()
```

{{% notice tip %}}
make sure that your #collision checking code is indent in the while loop
and also that the food.hideturtle() is indented under the if statement.
{{% /notice %}}

Here we have that if the distance between the turtle and cabbage is less than
 20 the cabbage (food) will hide.

Step 7.  Save and run the module, move your turtle to collide with the cabbage.

Now that works, we want to make the game more interesting as it will be a
 fairly boring game just to hide the cabbage. To make it more interesting what
 we will do is once the turtle collides (chomps) the cabbage we will move the
 cabbage to a random position.

For this to work we first need to import the random library at the top of your
 code just under the import math line:

```python

import random
```

Step 8.  Now you set the random position within the x and y coordinates by
 replacing the line `food.hideturtle` to:

```python
   
    if d < 20:
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))
```

Step 9.  Save and run the module. We now have the basis of our game
{{% notice note %}}
We set the random position at -290 and 290 and not -300 and 300 so the cabbage
 will not appear on the border.
{{% /notice %}}

Step 10.  Now you can use the same random position option to randomise where
 the cabbage appears at the start of the game by replacing the food.setposition
 under the #create food section:

```python
food.setposition(random.randint(-290, 290), random.randint(-290, 290))
```

Step 11.  Save and Run kbgame4

Your code should now look like this: [kbgame4.py](/python_game/src/kbgame4.py)

**Congratulations Module 4 Completed**
