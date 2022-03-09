---
title: "Links"
weight: 1
---

It's often useful to link webpages to each other.
Sometimes we want to link to another page within our website, and sometimes we want to link to another webpage entirely.

To link to a page we use an **anchor** element, which has the tagname `a`.
The `a` tag has an `href` attribute which has a value of a URL.

Here's an example:

```html
<a href="https://en.wikipedia.org/wiki/Turtle">Read more about turtles here.</a>
```

The above HTML would render like so:

[Read more about turtles here.](https://en.wikipedia.org/wiki/Turtle)


{{% notice challenge %}}

Add at least one link to another website to your page.

{{% /notice %}}

{{% notice tip %}}

When you click the link it takes us to that page in our CodePen window.
Instead, we could open that link in a new tab by adding `target="_blank"` to the `a` tag.
Try it!

{{% /notice %}}
