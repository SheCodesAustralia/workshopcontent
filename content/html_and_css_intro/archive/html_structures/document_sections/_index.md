+++
title = "Document Sections"
weight = 1
chapter = true
pre = "<b>1. </b>"
+++

One of the reasons we're using Codepen, is it takes care of a lot of the work for us in setting up the HTML page, so we can start writing, but most of the time we need to set up our HTML document to let the browser know how to read it.

When we start from scratch, the first element we need to include on our page is the `html` element, and all our website content will go inside that element.

```html
<html>
	<!-- Page content goes here -->
</html>
```

We also have the `head` element, which we can use to give the browser information about our webpage. This won't appear on the page, and is where we can give information about the title of our page (in a format the browser can understand).

```html
<html>
	<head>
		<!-- There is info for the browser here -->
	</head>
</html>
```

Most of our content goes inside the `body` element, this is content for the user which is typically visible in the browser.

```html
<html>
	<head>
		<!-- There is info for the browser here -->
	</head>
	<body>
		<!-- Visible page content goes here -->
	</body>
</html>
```

For the purposes of this workshop, all the HTML that we write in Codepen is being put inside our `body` element.