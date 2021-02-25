+++
title = "Font Weight"
weight = 2
chapter = true
pre = "<b>2. </b>"
+++

# Font Weight

We can also change the weight of our fonts, whether it's **bold** or normal (or somewhere in between). There's a few different ways that we can set the `font-weight` of our text, the first is using a named option, like `bold` or `normal`

```css
	h2 {
		font-weight: bold;
	}

	p {
		font-weight: normal;
	}
```

We can also use a numbered weight value, which is a number between 1 and 1000 (typically in increments of 100), with the higher numbers being a heavier weight (or bolder) text.

```css
	h2 {
		font-weight: 600;
	}

	p {
		font-weight: 400;
	}
```

While the named option gives less customisation, it relates to a specific numbered weight. `bold` will line up with a weight of `700` and `normal` will be `400`.

```css
	/* Both the h2 and p will have the same weight */
	h2 {
		font-weight: bold;
	}

	p {
		font-weight: 700;
	}
```

Try changing some of the text weights below.

{{< codepen id="ZEBvyQE" user="shecodesaus" title="CSS Properties - Font Weight" default="css,result" >}}