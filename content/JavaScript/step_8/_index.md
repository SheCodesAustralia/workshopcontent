---
title: "8. Keeping Score"
weight: 8
chapter: true
---

## Keeping Score - Count those Cupcakes!

Now that you're smashing cupcakes like a pro, it's time to keep track of your epic cupcake-smashing score! Every time you whack a cupcake, you earn a point. Let’s add a scoring system that updates in real-time on your scoreboard.

> Remember, right at the start we set the variable `scoreBoard`.

Now we're going to create another variable (this time called `score`) that starts at zero, and increases by one each time a cupcake is successfully smashed. This is your personal cupcake smash counter!

```diff
let scoreBoard = document.querySelector('.score');
+ let score = 0;

function smash(cupcake) {
	console.log('smashed!');

	cupcake.parentNode.classList.remove('up');
+	score = score + 1;
}
```

> Can you see the `smash` function? In this function, every time a cupcake is hit, we add 1 to the score.

We're also going to tell our `scoreBoard` variable to show `score` whenever it is increased. To update `scoreBoard` we will use the [textContent](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent) property.

```diff
function smash(cupcake) {
	console.log('smashed!');

	cupcake.parentNode.classList.remove('up');
	score = score + 1;
+	scoreBoard.textContent = score;
}
```

**Start** the game and watch your score increase everytime you smash a cupcake!

> **Resetting the score:** Each time we restart the game, we also want to reset the score back to zero, so we can start again from scratch.

```diff
function startGame() {
	timeUp = false;
+   score = 0;
+   scoreBoard.textContent = score;

	popUp();

	setTimeout(endGame, 10000);
}
```

Now each time you click **Start** you should see the score reset to zero.

## Check your code!

This is what you should have in CodePen so far:

```js
let timeUp = false;
let holes = document.querySelectorAll('.hole');
let scoreBoard = document.querySelector('.score');
	let score = 0;

function startGame() {
    timeUp = false;
		score = 0;
		scoreBoard.textContent = score;
	
    popUp();

    setTimeout(endGame, 10000);
}

function endGame() {
    timeUp = true;
}

function popUp() {
    console.log('Here I am!');
    let hole = holes[0];
    let time = 500;

    hole.classList.add('up');

    setTimeout(function () {
        hole.classList.remove('up');

        if (timeUp == false) {
            popUp();
        }
    }, time);
}

function smash(cupcake) {
    console.log('smashed!');

    cupcake.parentNode.classList.remove('up');
		score = score + 1;
		scoreBoard.textContent = score;
}
```
