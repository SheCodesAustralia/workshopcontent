---
title: "Colour"
weight: 3
---

The next thing we'll do is add some colour.
This will also help us to see where one section ends and another starts.

Add the following

```diff
/* Your CSS here */

+nav {
+	background-color: #87CEEB;
+}
```

{{% notice test %}}

The nav element should turn blue.

{{% /notice %}}

## Colours in CSS

Did you notice how we defined our colour.
We used a strange code instead (`#87CEEB`).
This is called a **Hex Code**, which is a 6 character code for representing colours in CSS.

There are several different ways of representing colours in CSS.

For exampple, there are some **name colours**.
The hex code we've used also has the name `skyblue`.

{{% notice challenge %}}

Try changing `background-color: #87CEEB;` to use `skyblue` instead of the hex code.

{{% /notice %}}

There only a few **named colours** in (216 to be exact!).
That might sound like a lot, but if we use hex codes instead that opens us up to over 16 MILLION colours instead!

We can also represent colours using **RGB codes** too.
For example, `skyblue` is represented as `rgb(135, 206, 235)` in RGB.

For the full list of named colours [check out this site](https://htmlcolorcodes.com/color-names/).

Or you could pick from every colour [using a picker](https://htmlcolorcodes.com/color-picker/).


## Colouring our Page

Let's get back to our CSS!

```diff
/* Your CSS here */

nav {
	background-color: #87CEEB;
}

+#section-3 {
+	background-color: #885A89;
+}
```

{{% notice test %}}

The background colour behind the cards should be purple.

{{% /notice %}}

{{% notice challenge %}}

Change the background colour of each card to `white`. Bonus: can you find the hex code for `white`?

{{% /notice %}}

{{% notice challenge %}}

Change the background colour of the each column in `section-5`.

{{% /notice %}}

{{% notice challenge %}}

Change the background colour of the `footer`.

{{% /notice %}}
