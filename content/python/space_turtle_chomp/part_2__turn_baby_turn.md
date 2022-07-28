+++
title = "Turn baby turn"
date = 2021-01-25T14:55:24+08:00
weight = 20
chapter = true
pre = "<b>2. </b>"
+++

### Part 2

# Turn baby turn


In part 2 we will assign keys on the keyboard to control the turtle and help
 it move left, right and speed up.

But before that we just need to understand a little bit about coding.
 Most developers do not write their code from top to bottom in one straight
 go and instead will write a bit of code, test it and then either add more,
 delete or edit the code.
 Throughout coding this tutorial you will need move to different parts of
 your program to add and edit. Be careful to read the instructions and make
 sure you are writing in the correct part of your program and not
 repeating lines you have already written.

Step 1.  A good habit to get into with any coding is to regularly save versions
 of your code as you make changes as this allows you to either re-use code for
 other programs or roll back to a working version if something goes wrong.
 So click File --> Save As and save the file as `kbgame2`

Step 2.  We need to set keyboard bindings that tell the computer that when you
 push a certain key to call a certain function. For this to work we need to set
 the computer to listen for keyboard strokes by typing the following under the
 speed = 1 line:

```python
speed = 1

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
while True:
    player.forward(speed)
```

We use the `turtle.onkey` method to set the computer to listen for a certain
 key and when that key is pressed it will run the assigned function. So when
 the left arrow key is pressed it will call the function called turn_left.

{{% notice note %}}
This new piece of code sits between setting the speed (line 12) and the start of the while loop (line 20). In Python where the code sits is very important
{{% /notice %}}

Step 3.  The next step is to write the `turn_left`, `turn_right` and
 `increase_speed` functions again under the speed = 1 line
 (you may need to press enter a few times to add some spare lines.

```python
speed = 1

# Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

```

`player.left` and `player.right` are set to turn your turtle at 30&deg; when
 the left and right arrow keys are pushed (remember to push and let go)
 global speed is a global function and we have set that every time the
 up arrow key is pushed the turtle increases its speed by 1.

Step 5.  Save the file by selecting File --&gt; Save and run your updated
 program by pressing F5 and then click on your turtle screen with the mouse
 and use the left and right arrow keys to move your turtle and the up arrow to
 increase its speed.

Step 6.  Close the Turtle and Python Shell windows.

Step 7.  You might see that the turtle icon jumps a bit when you press the
 arrow keys, this can be fixed very easily by adding the player speed variable
 at the end of your #Create player turtle section just after `player.penup()`.

```python

player.penup()
player.speed(0)
```

{{% notice info %}}
0 is the fastest animation speed.
{{% /notice %}}

Step 8.  Save and Run your module again try moving the turtle icon now and then
 close the Turtle and Python Shell windows.

Before moving to the next section have a play with your code you could change
 the angle the turtle moves when a either left or right key is pressed or you
 could add a slowdown function and keyboard binding using the 'Down' arrow.

Your code should now look like this: [kbgame2.py](/python_game/src/kbgame2.py)

**Congratulations Module 2 Completed**
