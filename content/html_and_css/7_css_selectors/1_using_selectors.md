---
title: "Using Selectors"
weight: 2
---

Take a look at the HTML provided to you.
You should notice that our `div` elements look a bit different to what we've seen before. They all have **classes** and **ids**:

```html
<div class="first-row" id="box-1">
  <p>Box 1</p>
</div>
<div class="first-row" id="box-2">
  <p>Box 2</p>
</div>
<div class="second-row" id="box-3">
  <p>Box 3</p>
</div>
<div class="second-row" id="box-4">
  <p>Box 4</p>
</div>
```

We'll use type, class and ID selectors to change the colour of different elements on the page.

## Type Selectors

First, let's change the colour of the text.
We can use a **type selector** to do this.
By referencing the `p` tag, we can change the colour of all text in a `p` tag.
Add the following to your css:

```diff
/* Your CSS here */

body {
  background-color: orange;
}

+p {
+  color: blue;
+}
```

{{% notice test %}}

The text should now be blue.

{{% /notice %}}

## ID Selectors

Each box has a unique `id`, which means that we can reference each box individually.

Let's try changing the background colour of `box-1` only:

```diff
/* Your CSS here */


body {
  background-color: orange;
}

p {
  color: blue;
}

+#box-1 {
+  background-color: hotpink;
+}

```

{{% notice test %}}

The top left box should now be pink.

{{% /notice %}}

## Class Selectors

The top two boxes have the `first-row` class, and the bottom two boxes have the `bottom-row` class.
This means that we could use these classes to reference each row individually, i.e. two boxes at a time.

Let's try changing the background colour of the two boxes in the bottom row:

```diff
/* Your CSS here */

body {
  background-color: orange;
}

p {
  color: blue;
}

#box-1 {
  background-color: hotpink;
}

+.second-row {
+  background-color: yellow;
+}
```

{{% notice test %}}

The bottom boxes should now be yellow.

{{% /notice %}}


This should be the final result:

![](../../images/boxes_complete.png)


{{% notice challenge %}}

Try changing the background colour of box 2 only.

{{% /notice %}}
