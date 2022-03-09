---
title: "Borders"
weight: 6
chapter: false
---

We can also add borders to elements.

Try adding the following to the first image:

```diff
/* Your CSS here */

header img {
	height: 100px;
+	border: 1px solid #000000;
}
```

{{% notice test %}}

You should see a thin black border appear around the first image.

{{% /notice %}}

`border: 1px solid #000;` is short hand for "create a border that is `1px` wide, solid and black.

{{% notice challenge %}}

Try changing the width and colour of the border.

{{% /notice %}}

{{% notice challenge %}}

There are several different border styles - [here\'s a list of them](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style).
Try changing the style of the border.

{{% /notice %}}

{{% notice challenge %}}

Add a border to each card.

{{% /notice %}}

Here's what your page should look like so far:

![](../../images/animals_borders.jpeg)
