---
title: "7. Smash It"
weight: 7
chapter: true
---

## Smashing the cupcakes

Now that our cupcakes are merrily popping up and down like little party crashers, let's write a function to 'smash' them!

To do this, we're going to create another function called `smash` to run whenever you click on a cupcake. When you do, the cupcake will disappear as if it's been perfectly smashed! To make this happen, we remove the `up` class from the hole the cupcake is in so that the smashed cupcake pops down again.

Add the following function to the bottom of your code:

```js
function smash(cupcake) {
    console.log('smashed!');

    cupcake.parentNode.classList.remove('up');
}
```

When we created the HTML code in the template, we actually already instructed the button to run this function when it is clicked (feel free to peek at the HTML code and see this for yourself). Press **Start** and start smashing cupcakes! Whenever you click a cupcake it will disappear again, and a message will appear in the console.

<p align="start">
<img src=../step_2/shecodes_cupcake.svg width="20">
</p>

> You may have noticed that we're using this thing called a `parentNode`. Up until now, we have been referencing the hole elements in the HTML, but now we want to reference the cupcake itself (which is inside the 'hole' element). 
> 
> In our HTML, the cupcake that we click on is a 'child' of the hole it is popping up from, so the `.parentNode` part tells JavaScript to look for the hole that the cupcake is appearing from, rather than the cupcake itself.
You can read more about nodes and parent nodes [here](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentNode).

<p align="start">
<img src=../step_2/plain_cupcake.svg width="20">
<img src=../step_2/plain_cupcake.svg width="20">
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
}
```

### Console Celebrations:
The `console.log('smashed!')` line is a fun way to celebrate your cupcake-smashing skills. Check out your console (remember, in CodePen's bottom left) to see the feedback each time you smash a cupcake.
