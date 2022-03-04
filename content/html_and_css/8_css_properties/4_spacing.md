---
title: "Spacing"
weight: 4
---

Now that we've added some colour, it makes the awkward spacing around elements a bit more obvious.

Let's fix that!
Again, we'll start at the top and work our way down.

## Step 1

At the moment, the nav is exactly as tall as the text inside it.
Let's add some space between the end of the nav and the text.
We can do this using the `padding` property.

Add the following to your css:

```diff
/* Your CSS here */

nav {
	background-color: #87CEEB;
+	padding: 10px;
}
```

{{% notice test %}}

There will now be more space in the nav around the text.

{{% /notice %}}

## Step 2

Let's also modify the `padding` of the header div to add space around the image:

```diff
/* Your CSS here */

nav {
	background-color: #87CEEB;
	padding: 10px;
}

+header div {
+	padding: 20px;
+}
```

{{% notice test %}}

There should now be a gap between the nav and the image.

{{% /notice %}}

## Step 3

Next let's add some space around `section-2`:

```diff
/* Your CSS here */

nav {
	background-color: #87CEEB;
	padding: 10px;
}

header div {
	padding: 20px;
}

+#section-2 {
+	padding: 20px 0px;
+}
```

{{% notice test %}}

There will now be a gap between the images and `section-3`.

{{% /notice %}}

Did you notice how we did this padding a little differently?
Instead of specifying one value, we provided two, i.e. `padding: 20px 0px;` rather than `padding: 20px`.

Padding actually takes 4 values: top, right, bottom, left.

Often we want to add the same amount of padding to all four sides of an element, so we can use`padding: 20px` as shorthand for `padding: 20px 20px 20px 20px`.

We also often find ourselves wanting one amount of padding for the top and bottom of an element, and a different amount for the left and right.
`padding: 20px 0px;` is short hand for `padding: 20px 0px 20px 0px;` and means "use `20px` of padding for the top and bottom, and none for the right and left`.

## Step 4

The next section has the cards.

First, let's add padding to the section itself:

```diff
#section-3 {
	background-color: #885A89;
+	padding: 20px;
}
```

{{% notice test %}}

There will now be space between the edge of the purple background and the white cards.

{{% /notice %}}

{{% notice challenge %}}

Add `20px` of padding to each of the cards.

{{% /notice %}}

## Step 5

{{% notice challenge %}}

For `section-4` and each `.column`, add `20px` of `padding` to the top and bottom, and `0px` of `padding` to the left and right.

{{% /notice %}}

{{% notice challenge %}}

Add `10px` of `padding` to the footer.

{{% /notice %}}


## Step 6

So far we've used `padding` to put space in an element.
In other words, `padding` is the space between an elements border and the content inside it.

But what if we wanted to put space between elements?
We can use `margin` to achieve this.

Try adding the following to your CSS:

```diff
.card {
	height: 250px;
	width: 25%;
	display: inline-block;
	vertical-align: middle;
	background-color: #fff;
	padding: 10px;
+	margin: 0 10px;
}
```

{{% notice test %}}

There should now be space between the cards. Try changing `10px` to a larger number to make it easier to see if necessary.

{{% /notice %}}

You might find this graphic useful in comparing margin and padding:

![Graphic showing CSS box model.](../../images/box_model.png)

(We'll get to the border property shortly...)


**Great job! Done!**

![](../../images/gifs/celebration_2.gif)
