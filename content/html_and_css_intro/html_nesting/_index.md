+++
title = "Nesting HTML"
weight = 4
chapter = true
pre = "<b>4. </b>"
+++

# Nesting HTML Elements

So far we've just been writing content inside our HTML elements, but did you know that you can nest other HTML elements inside them as well?

```html
<p>I have a paragraph of text here, which also has a <a href="https://google.com">link</a> inside it!</p>
```

Being able to nest elements like this is important to be able to do things like include a link within a paragraph of text, but it's also important when we start to build a more complicated webpage, with structure and different sections of content.

Now as you might expect, you can't nest content inside a self-closing element (there aren't any opening and closing tags to put another element between), but you can include a self-closing element inside a regular element, for example including an image inside a paragraph.

```html
<p>I have a paragraph of text here, and inside the paragraph, I also have an image <img src="https://quokkas.amyskapers.dev/img/quokka_(1).jpg" />, which is related to the content of the paragraph and therefore I want it to appear with the text.</p>
```

Depending on what elements we're embedding, we also want to indent our code as well. This isn't necessary for our code to work, but nesting elements helps us to see and recognise when elements are nested inside one another. This gets especially important when we start to get several levels deep.

```html
	<!-- Link nested inside a heading -->
	<h2><a href="/page">Linked Heading</a></h2>

	<!-- Indenting nested link -->
	<h2>
		<a href="/page">Linked Heading</a>
	</h2>
```