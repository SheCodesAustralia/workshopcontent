+++
title = "Size"
weight = 3
chapter = true
pre = "<b>3. </b>"
+++

# Size

For the most part our browser is pretty smart, and will automatically change the size of an element depending on how much content it has inside it.

But sometimes we want to be able to control the size of our elements as well, which we can do by setting the `width` and/or `height` on them.

```css
img {
	height: 300px
}
```

Similar to setting the size of text, we can use `px` as our unit, but we may also want to use percentages, so the content size changes depending on the size of our screen.

```css
p {
	width: 50%
}
```

Try editing the Codepen below to make the images (`img`) only 300px tall, and the paragraphs (`p`) take up only 70% of the screen width

{{< codepen id="ZEBvyXb" user="shecodesaus" title="CSS Properties - Size" default="css,result" >}}
