---
title: "Fonts"
weight: 5
---

There are a lot of different things we can do with fonts, including changing their family and size.

## Family

Head over to [Google Fonts](https://fonts.google.com/) and pick out a font that you like.

Select that font then view all your selected fonts:

![Screenshot of Google Font.](../../images/fonts_1.png)

Select the `@import` option:

![Screenshot of how to use Google Font](../../images/fonts_2.png)

Copy the code **between the `<style>` tags**.

Past this code at the **top of your css file**.

```diff
/* Your fonts here */
+@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
/* */
```

Then head back to Google Fonts and copy the `font-family` line of code.

Let's style our headings with your selected font:

```diff
/* Your CSS here */

+h1 {
+	font-family: 'Pacifico', cursive;
+}

+h2 {
+	font-family: 'Pacifico', cursive;
+}

+h3 {
+	font-family: 'Pacifico', cursive;
+}
```

{{% notice challenge %}}

Find another font to use for the nav, footer and paragraphs.

{{% /notice %}}

## Size

Let's try changing the size of our text too.

Add the following to your CSS:

```diff
/* Your CSS here */

h1 {
	font-family: 'Pacifico', cursive;
+    font-size: 50px;
}
```

{{% notice challenge %}}

Change the font size of the `h2`, `h3`, and `p` tags.

{{% /notice %}}

## Colour

We can change the color of our fonts using the `color` attribute.

Add the following to your CSS:

```diff
/* Your CSS here */

+a {
+	color: #ffffff;
+}
```

{{% notice test %}}

The colour of the `a` tags in the `nav` should turn white.

{{% /notice %}}

{{% notice challenge %}}

Change the colour of the `h1`, `h2` and `h3` headings.

{{% /notice %}}
