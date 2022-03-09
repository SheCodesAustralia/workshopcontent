---
title: "Nav"
weight: 3
chapter: true
---

The `nav` (aka "navigation") is used to provide links that navigate to other webpages.

Let's wrap our three links in opening and closing `nav` tags:

```diff
<header>
+  <nav>
    <a href="https://en.wikipedia.org/wiki/Turtle">Wikipedia</a>
    <a href="https://www.worldwildlife.org/species/sea-turtle">WWF</a>
    <a href="https://www.britannica.com/animal/turtle-reptile">Britannica</a>
+  </nav>
  <img src="https://assets.codepen.io/5804361/Myrtle_Game.gif" alt="Gif of computer game with turtle moving around a grid."/>
  <h1>Myrtle the Turtle</h1>
</header>
```

{{% notice test %}}

The background of the nav should appear as darker pink.
The links should be on the right, each with a white background.

{{% /notice %}}
