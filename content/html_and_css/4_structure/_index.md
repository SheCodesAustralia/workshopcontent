---
title: "Structuring our Page"
weight: 4
---

So far we’ve learnt a couple of different elements, but HTML isn’t just about defining the content of the page, it is also used to define the page structure.
We can also use HTML elements to give the browser information about the structure of the page, and other information it needs to display your website.

One of the reasons we're using Codepen, is it takes care of a lot of the work for us in setting up the HTML page, so we can start writing, but most of the time we need to set up our HTML document to let the browser know how to read it.

When we start from scratch, the first element we need to include on our page is the `html` element, and all our website content will go inside that element.

```html
<html>
    <!-- Page content goes here -->
</html>
```

We also have the `head` element, which we can use to give the browser information about our webpage.
This won't appear on the page, and is where we can give information about the title of our page (in a format the browser can understand).

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

Fortunately, Codepen takes care of a lot of the structure for us, so we only have to worry about the visible page content.
All the HTML we write is being put inside the `body` element.

Next we are going to learn how to structure the content in the `body`.

Todo this, we are going to build a webpage step by step.
When we're done, our page will look like this:

![Screenshot of webpage with different background colours for each element type.](../images/myrtle_the_turtle_preview.png.png)

We've already written some CSS for you, this is what gives the page colour and layout.

You'll know if you've built your page correctly because it should look identical in colour and layout to the above screenshot.

Once again, we've created a template for you to get started with.
Open the template by [clicking this link](). TODO

Once you've opened the pen, click the `fork` button on the bottom left of the page to make a copy of the pen under your account.

![Screenshot of CodePen with "fork" button highlighted.](../../images/forking_a_pen.png)

