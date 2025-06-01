---
title: "3. Cupcakes are Forever"
weight: 3
chapter: true
---

# Popping Up Cupcakes

Next we want to create a function to pop our cupcakes up out of the holes. There's CSS styling already set up for most of this so the cupcakes will appear all shiny, so we just need to add a class to one of our holes to make the cupcakes appear. This will take the first hole from the list we saved earlier, and add the class of `up` to it (which will then do some CSS magic). Add the following to the bottom of your JavaScript code:

```js
function popUp() {
    let hole = holes[0];

    hole.classList.add('up');
}
```

Now instead of adding a comment in the console log at the start of the game, we can trigger our `popUp` function to run when the game starts. Under where you first defined your `startGame` function, remove the `console.log` line and add the `popUp` function trigger.

{{% notice info %}}

Note the different colours and +/- indicators in the code example below. This is instructing you to remove the `console.log` line, and add the `popUp` line, but without the `+` and `-` symbols. If you're not sure what to do, the completed code up to this point is provided at the end of this page.

{{% /notice %}}

```diff
function startGame() {
-	console.log('Game has started');
+	popUp();

	setTimeout(endGame, 10000);
}
```

Now try clicking the **Start** button and see what happens! A cupcake should have appeared form the first hole.

## Check your code!

This is what you should have in CodePen so far:

```js
let timeUp = false;
let holes = document.querySelectorAll('.hole');
let scoreBoard = document.querySelector('.score');

function startGame() {
    popUp();

    setTimeout(endGame, 10000);
}

function endGame() {
    console.log('Game has finished');
}

function popUp() {
    let hole = holes[0];

    hole.classList.add('up');
}
```
