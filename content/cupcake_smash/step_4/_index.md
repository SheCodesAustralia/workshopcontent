---
title: "4. Game OVER"
weight: 4
chapter: true
---

# Ending the Game

Before we go too much further with our cupcakes, let's edit the `endGame` function we created earlier so that instead of publishing a message to the console, it changes the value stored in our `timeUp` variable to `true.`

```diff
function endGame() {
-	console.log('Game has finished');
+	timeUp = true;
}
```

We'll also need to make sure we set `timeUp` back to false when the game starts again.

```diff
function startGame() {
+	timeUp = false;
	popUp();

	setTimeout(endGame, 10000);
}
```

## Check your code!

This is what you should have in CodePen so far:

```js
let timeUp = false;
let holes = document.querySelectorAll('.hole');
let scoreBoard = document.querySelector('.score');

function startGame() {
    timeUp = false;
    popUp();

    setTimeout(endGame, 10000);
}

function endGame() {
    timeUp = true;
}

function popUp() {
    let hole = holes[0];

    hole.classList.add('up');
}
```
