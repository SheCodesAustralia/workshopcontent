+++
title = "Borders"
weight = 5
chapter = true
pre = "<b>5. </b>"
+++

We can also use CSS to add borders to each of our elements, and customise how those borders look.

There's three different properties used for our borders, `border-width`, `border-style` and `border-color`.

The `border-width` allows us to set the thickness of our border, typically set using `px`.

```css
	img {
		border-width: 5px;
	}
```

We can then use the `border-style` property to set the style of border we want, it could be `solid`, `dotted`, `dashed`, `double`, `inset` or a [range of other options](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style#values).

```css
	img {
		border-width: 5px;
		border-style: solid;
	}
```

We can then use `border-color` to set the colour of our border, using one of the different ways we have available to define our colours.

```css
	img {
		border-width: 5px;
		border-style: solid;
		border-color: chartreuse;
	}
```

Now because this can be a lot of code to write, and we'll pretty much always want to use all three of these properties, we can also use the shorthand property, `border` for setting them all at once. This property allows us to define the `border-width`, `border-style` and `border-color` in one line (in that particular order), separating each value with a space.

```css
img {
	border: 2px solid chartreuse;
}
```

Try adding borders to the different elements in the Codepen below. See what different colour and style combinations you can come up with!

{{< codepen id="BaQJZbg" user="shecodesaus" title="CSS Properties - Borders" default="css,result" >}}

