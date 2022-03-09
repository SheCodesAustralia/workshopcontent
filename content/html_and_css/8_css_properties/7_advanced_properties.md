---
title: "Advanced Properties"
weight: 7
---

WOW! We've done a lot!

If you've been through every step of this tutorial, then your page should look like this:

![Screenshot of website so far.](../../images/animals_borders.png)

It's looking pretty good!
Let's add some fun styles now...


## Paralax

Firstly, what's with that big gap between the heading and the "Popular Photos"?
We've been saving it for a photo...

We can insert images using CSS.
Add the following to your CSS file:

```diff
#section-1 {
	height: 300px;
+	background-image: url("");
}
```

[Here\'s an image url you can use.](https://images.unsplash.com/photo-1518709594023-6eab9bab7b23?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1025&q=80)

That will insert the image as the background for the `section-1` element.

{{% notice test %}}

Make sure you can see the image appear on the page.

{{% /notice %}}

Next, we'll position it a bit better so we can see the center of the image:

```diff
#section-1 {
	height: 300px;
	background-image: url("");
+    background-position: center;
+    background-size: cover;
}
```

Finally, we'll fix it in place.
This means that we we scroll the image will appear as if it is staying in place, creating a cool paralax effect.

Add the following to your css:

```diff
#section-1 {
	height: 300px;
	background-image: url("");
    background-position: center;
    background-size: cover;
+	background-attachment: fixed;
}
```

{{% notice test %}}

Scroll and see what happens!

{{% /notice %}}


## Gradients

So far we've just used solid colours for our backgrounds, but we can actually make gradients too.

Try changing your CSS to use a gradient behind the cards:

```diff
#section-3 {
- 	background-color: #885A89;
+	background: linear-gradient(90deg, #885A89 0%, #87A1EB 100%);
	padding: 20px;
}
```

{{% notice challenge %}}

Have a play with the direction and colours of the gradient.
Here's a cool [tool for creating gradients](https://cssgradient.io/) if you need inspiration.

{{% /notice %}}

## Shadows

We could also add some shadows to make some elements feel as though they are lifted from the page.

Try adding a shadow to the `h1` text:

```diff
h1 {
	font-family: 'Pacifico', cursive;
	font-size: 50px;
+	text-shadow: 1px 1px 2px #000000;
}
```

And try adding a shadow to the cards:

```diff
header img {
	height: 100px;
	border: 1px solid #000;
+	box-shadow: 1px 1px 2px #000000;
}
```

{{% notice challenge %}}

Try adding text or box shadows to other elements!
Here's a [handy tool for generating shadows](https://webcode.tools/generators/css/box-shadow).

{{% /notice %}}
