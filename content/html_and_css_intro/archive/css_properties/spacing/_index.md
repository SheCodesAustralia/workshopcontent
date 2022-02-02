+++
title = "Spacing"
weight = 4
chapter = true
pre = "<b>4. </b>"
+++

# Spacing

We also want to make sure that our content is nicely spaced, white space is like Vegemite (you don't want too much, or too little, just the right amount).

To add space between our content, we can use two different properties, `margin` and `padding`. Padding adds space around the content, but within the element, while margin adds space around the element (between it and other elements).

![](images/margins_padding.png)

We set `margin` and `padding` the same way, using four values separated by a space, starting at the top and going clockwise around the element.

```css
p {
	/* Top Right Bottom Left */
	margin: 20px 15px 10px 20px;
	padding: 10px 10px 10px 10px;
}
```

Both the `margin` and `padding` will also infer values based on what they're given. If only one value is given, it will be applied to all four sizes, and if a side has a missing value, it will get it's value from it's pair (top and bottom or right and left).

```css
p {
	/* Margin of 10px will be applied to all four sides */
	margin: 10px;

	/* Padding of 10px will be applied to the top and bottom, and 20px will be applied to the right and left sizes */
	padding: 10px 20px;

	/* Margin of 10px will be applied to the top, 20px to the right and left sides and 15px to the bottom */
	margin: 10px 20px 15px;
}
```

Try adding spacing to the elements in the Codepen below, so that there's a large margin above every `h2` element, and a 50px padding on the left side of each paragraph.

{{< codepen id="OJbzgdG" user="shecodesaus" title="CSS Properties - Spacing" default="css,result" >}}
