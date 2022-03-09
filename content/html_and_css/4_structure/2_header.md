---
title: "Header"
weight: 2
chapter: true
---

The `header` element is used for introductory content.
This is usually the main heading for the page and the navigation bar.

Let's wrap our nav, h1 and image in the header:

```diff
+<header>
  <a href="https://en.wikipedia.org/wiki/Turtle">Wikipedia</a>
  <a href="https://www.worldwildlife.org/species/sea-turtle">WWF</a>
  <a href="https://www.britannica.com/animal/turtle-reptile">Britannica</a>
  <img src="https://assets.codepen.io/5804361/Myrtle_Game.gif" alt="Gif of computer game with turtle moving around a grid."/>
  <h1>Myrtle the Turtle</h1>
+</header>
```

{{% notice test %}}

The background of the header should appear pink.

{{% /notice %}}

