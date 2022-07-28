+++
title = "Setting the boundaries for cabbage"
date = 2021-01-25T14:55:24+08:00
weight = 60
chapter = true
pre = "<b>6. </b>"
+++

### Part 6

# Setting the boundaries for cabbage

So what you will do next is make the food move around the screen, this is
 fairly easy to do by using the same forward option we used for your player.

Step 1.  Within the While Loop add the following code after the #Boundary
 Checking Player y coordinate code:

```python
    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)

    # Move food around
    food.forward(1)
```

Step 2.  Save your game as kbgame6 and run the module

Step 3.  Now your cabbage moves across the screen but at the moment it always
 moves to the right, so let make the game more interesting by using the random
 function again by adding the following to the end of the # Collision checking
 section:

```python
    food.right(random.randint(0, 360))
```

Step 4.  The food is moving rather slow so let’s speed it up by changing the
 forward speed to 3 by updating food.forward with:

```python
# Move food around
    food.forward(3)
```

Step 5.  Save and run your module, have a play with different speeds.
 Your food is now moving around the screen in a random direction. The only
 problem we have is that it can move off the screen. This is an easy fix as you
 can cut and paste the same code you wrote for your turtle for border checking
 and modify it for the food.

Step 6.  Cut the following code and paste it directly underneath making sure
 the indents are aligned

```python
    # Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290::
        player.right(180)

    # Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)  
```

Step 7. Edit the pasted code to change player to food:

```
    # Boundary Food Checking x coordinate
    if food.xcor() > 290 or food.xcor() < -290:
        food.right(180)

    # Boundary Food Checking y coordinate
    if food.ycor() > 290 or food.ycor() < -290:
        food.right(180) 
```

Now when your space cabbage hits the boundary it will bounce of the wall at
 180&deg; just like your turtle

Step 7.  Save and run your module

Before moving on have a play at modify your code changing the bounce angle and
 speed of the space cabbage.

Your code should now look like this: [kbgame6.py](/python_game/src/kbgame6.py)

**Congratulations Module 6 Completed**
