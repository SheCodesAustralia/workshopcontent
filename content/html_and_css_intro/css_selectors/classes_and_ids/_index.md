+++
title = "Classes and IDs"
weight = 1
chapter = true
pre = "<b>1. </b>"
+++

## Classes and IDs

We can add classes and IDs to our HTML elements, as attributes, similar to how we referenced the URL of an image.

```html
<p class="content" id="my-paragraph">I am a paragraph of text</p>
```

Although they offer similar functionality, there's a slight difference between them.

## Classes

Classes can be added to multiple elements, and elements can have multiple classes, these are used to create a group with a class being used to refer to the group.

A class is like a last name, other people might have the same last name as you, some people might have multiple last names and other people might have no last name.

```html
<h2 class="heading feature">My heading</h2>
<h2 class="heading">Another heading</h2>

```

## IDs

IDs on the other hand, are unique, with each element only having one ID and only one of that ID being allowed on the page.

An ID is like a tax file number, not everyone has one, but you can only have one, and no one has the same as you.

```html
<h2 id="section-1">My heading</h2>
<p>Paragraph of text</p>
```

Most of the time if we need to use a class or ID, we'll be using a class. The main times we use an ID is to refer to something we know is unique.