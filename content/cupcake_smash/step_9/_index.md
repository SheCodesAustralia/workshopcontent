---
title: "9. That's So Random!"
weight: 9
chapter: true
---

## Let's mix it up - randomising the cupcakes!

Great job on getting your game running so far! Now it's time to add a twist ... we obviously don't want the cupcake to always pop up in the first hole because that would make for a pretty boring (and easy) game! Instead we'll create a new function to randomly pick which hole the cupcake will appear in.

At the moment our `popUp` function looks like this:

```js
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

The part of this code that determines where the cupcake pops up is this line:

```js
let hole = holes[0];
```

Right now, your code always picks the first hole.

Remember right back at the start when we created our `holes` variable? We wrote a line that looked like:

`let holes = document.querySelectorAll('.hole');`

In that step we're telling JavaScript "Hey, find me all the cupcake holes on the page and put them into a neat list!" This list is what programmers call an **array**. It might look something like this: 

`holes = [hole 0, hole 1, hole 2, hole 3, ... hole 8]`.

Yes you are seeing this correctly, in JavaScript, **arrays start counting at 0**. So, the`[0]`in`holes[0]` is what tells JavaScript to just get the first cupcake hole on the page.

<p align="start">
<img src=../step_2/plain_cupcake2.svg width="20">
</p>

> It might seem a little strange at first, I know usually we start counting at 1. But think of it like this: if the cupcake holes were secret hideouts, the code '0' is the secret agent name for the first one!

> To recap, our `holes` variable type is called an '[array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)' and looks something like this: `holes = [hole 0, hole 1, hole 2, ... hole 8]`. We can reference any item in our array using the index position (what position it is in in the list). And remember, in arrays the first position is always '0' (not 1). So if we reference `holes[1]` it will actually access the second cupcake hole, not the first!

<p align="start">
<img src=../step_2/test_plain_cupcake.svg width="20">
</p>

Now remember our goal: to randomly generate a number between 0 and 8 (because we have 9 holes) that we can use to reference one of the holes in our array, rather than always getting the first one. To do this we are going to create our own function called `randomHole` which will use JavaScript's built in [`math.floor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor) and
the [`math.random`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) functions.

At the bottom of your existing code, add this:

```js
function randomHole(holes) {
    let holeNumber = Math.floor(Math.random() * holes.length);
    let hole = holes[holeNumber];

    return hole;
}
```

We then need to update our `popUp` function to run our new `randomHole` function each time the cupcake pops up, instead of always referring to the first hole:

```diff
function popUp() {
-	let hole = holes[0];
+   let hole = randomHole(holes);
	let time = 500;

	hole.classList.add('up');

	setTimeout(function() {
		hole.classList.remove('up');

		if(timeUp == false) {
				popUp();
		}
	}, time)
}
```

Now when you hit **Start**, you should see your cupcakes popping up everywhere!

<p align="start">
<img src=../step_2/shecodes_cupcake.svg width="20">
<img src=../step_2/shecodes_cupcake.svg width="20">
<img src=../step_2/shecodes_cupcake.svg width="20">
</p>

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
    let hole = randomHole(holes);
    let time = 500;

    hole.classList.add('up');

    setTimeout(function () {
        hole.classList.remove('up');

        if (timeUp == false) {
            popUp();
        }
    }, time);
}

function randomHole(holes) {
    let holeNumber = Math.floor(Math.random() * holes.length);
    let hole = holes[holeNumber];

    return hole;
}

function smash(cupcake) {
    console.log('smashed!');

    cupcake.parentNode.classList.remove('up');
    score = score + 1;
    scoreBoard.textContent = score;
}
```
<p align="start">
<img src=../step_2/plain_cupcake.svg width="20">
</p>

> **Learning in Action:** You're using arrays and random number generation - key concepts in JavaScript!

<p align="start">
<img src=../step_2/shecodes_cupcake.svg width="20">
<img src=../step_2/shecodes_cupcake.svg width="20">
<img src=../step_2/shecodes_cupcake.svg width="20">
</p>

### Extra challenge

Once you're comfortable, experiment with different timings or even try changing the random number generation logic to see how it affects the game's behaviour. What happens if you use `Math.round()` instead of `Math.floor()`?
