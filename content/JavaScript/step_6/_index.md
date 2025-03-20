---
title: "6. What If..?"
weight: 6
chapter: true
---

## What If?

Now that we have got our cupcake bobbing in and out, we want to repeat this over and over again until the time is up. We're going to use one of the most useful and powerful bits of programming to do this - the `if` statement. We can use this to check a condition and take a different action depending on whether it is `true` or `false`.

```diff
function popUp() {
	let hole = holes[0];
	let time = 500;

	hole.classList.add('up');

	setTimeout(function() {
		hole.classList.remove('up');

+		if (timeUp == false) {
+			popUp();
+		}

	}, time)
}
```

{{% notice tip %}}

Let's break that down! The `if` tells JavaScript we are about to use an if statement. The part in the parentheses `()` is the 'condition', which is what we are using to make a decision. In this case, we are checking if our `timeUp` variable is currently set to `false`. If `timeUp` is `false`, then the code inside the curly braces `{}` will be run, otherwise this code is ignored. You can read more about if statements in JavaScript [here](https://javascript.info/ifelse).

{{% /notice %}}

Now when you hit **Start** your cupcake will continually pop up and down - but only on the same hole and it's happening so fast that we can't even see it! We'll fix this up in the next step by randomising which hole it pops up from. For now, to test that it really is working, let's add a message to the console.

```diff
function popUp() {
+	console.log('Here I am!');
	let hole = holes[0];
	let time = 500;

	hole.classList.add('up');

	setTimeout(function() {
		hole.classList.remove('up');

		if (timeUp == false) {
			popUp();
		}

	}, time)
}
```

You should now see the same message ('Here I am!') appearing in the console over and over again.

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
```
