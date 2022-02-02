+++
title = "Lists"
weight = 1
chapter = true
pre = "<b>1. </b>"
+++

# Lists

We can also add lists in our html, there are two different kinds of lists we can use, **ordered** (numbered) and **unordered** (bulleted) lists.

Ordered lists use the `ol` (ordered list) element, and we can nest individual `li` (list item) elements inside it, for each of the list items.

```html
<h1>HTML and CSS Workshop</h1>

<ol>
	<li>Intro to HTML</li>
	<li>HTML Elements</li>
	<li>HTML Attributes</li>
	<li>Nesting HTML</li>
</ol>
```

Similarly, unordered lists use the `ul` (unordered list) element, and we nest `li` elements inside it.

```html
<h1>She Codes Workshops</h1>

<ul>
	<li>HTML and CSS</li>
	<li>Python</li>
	<li>WordPress</li>
</ul>
```

Try making some lists of your own, see what happens if you change a list from a unordered to an ordered list.

{{< codepen id="LYbeYMd" user="shecodesaus" title="HTML Elements - Lists" >}}

{{% notice tip %}}
Fun Fact: You can nest lists inside lists, see what that looks like
{{% /notice %}}