+++
title = "Space Turtle Chomp"
date = 2021-01-25T14:55:24+08:00
weight = 10
chapter = true
pre = "<b>1. </b>"
+++


### Part 1

# Space Turtle Chomp

We will start off today creating a simple Python game using Python Turtle
 Graphics. Turtle Graphics is a prebuilt set of python instructions that allow you
 to create and move characters around the screen allowing you to draw pictures,
 logos and create simple animations or games.

Step 1.  If not already open please open VS Code.  
You should see your Terminal / Command Prompt window.

Step 2.  Select File --&gt; New File you should see your program window

Step 3.  As it is a great idea to save your project at the beginning of any new
 development, select File --&gt; Save and name the file, I called mine kbgame1.

Step 4. When coding one of the first things we should always do as a developer is leave a comment explaining what the program does at the top of the screen.

Write the below on the top line:

```python
# Turtle Graphics Game – Space Turtle Chomp
```

Step 5. Next we need to import the Turtle libraries and set up the screen, we do this by typing:

{{% codecaption title="kbgame1.py" %}}

```python
import turtle

# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')
```

{{% /codecaption %}}


`turtle.setup` sets the size of the Turtle game window \(it’s not necessary
 but helps when using different screen sizes\).
 `wn` is the name we are calling the screen \(as we learnt in the Python
 introduction all variables need a name\). `bgcolor` allows us to set the
 background colour. There are lots of colours to choose from.
![colour chart](/python_game/100_Color_names_python.png)

{{% notice note %}}
note the American spelling of color, this is something to watch out for when
 programming.
{{% /notice %}}

{{% notice tip %}}
It is good practice to leave a comment \(\#\) before your code so you can
 remember what it does
{{% /notice %}}

Step 6. Next we create our first Turtle character, we do this by typing:

```python
# Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()
```

So we create a new turtle variable called player then use the inbuilt turtle
 attributes to help set it up, `player.color` \(again we can select a different
 colour from the color chart). `player.shape` selects the shape \(you can also
 use circle, arrow, square and classic\). `Penup` means that the turtle shape
 won’t leave a line went it moves \(think of a pen in your hand, penup\(\)
 you don’t draw, pendown\(\) you do draw.

Step 7. Now we set the speed we want our turtle to move across the screen at:

```python
# Set speed variable
speed = 1
```

Step 8: Finally we need the Turtle to move and the easiest way to do this is by
 setting a while loop:

```python
while True:
    player.forward(speed)
```

This will now continue to move your turtle forward across the screen at a speed of 1.

{{% notice note %}}
note the indent of the player.forward… this needs to be there for the code to work.
{{% /notice %}}

Step 9: Now all we need to do is save our code, we can do this by selecting File
 --&gt; Save \(Ctrl S on Windows or Cmd S on Mac\).Then run the module by
 selecting Run --&gt; Run Module \(or pressing F5\)

You should see two windows open up a Python Shell window that will have
 “Python 3.6.1 \(v3.6.1:69c0db5, Mar 21 2017, 17:54:52\) \[MSC v.1900 32 bit \(Intel\)\]…”
 or something similar written on it and your Turtle window with a Navy
 background and Dark Orange turtle moving across the screen. Close both the
 shell and turtle window to return to your programming code.

Before moving onto the next section you can have a play with your code by
 trying different colours, shapes and speeds and for some fun you could change
 `player.penup()` to `player.pendown()`

Your code should now look like this: [kbgame1.py](/python_game/src/kbgame1.py)

**Congratulations Module 1 Completed**
