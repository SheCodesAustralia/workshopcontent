+++
title = "Using Classes and IDs in CSS"
weight = 2
chapter = true
pre = "<b>2. </b>"
+++

## Using Classes and IDs in CSS

Once we have have classes and IDs on our HTML elements, we can start using them in our CSS (similar to how we've been referencing HTML tag names).

To reference a particular class in CSS, we need to prefix it with a `.`, eg. `.class-name`.

```css
.feature {
	color: rebeccapurple;
}
```

To reference an ID in CSS, we need to prefix it with a `#`, eg. `#my-id`.

```css
#header {
	background: lightsalmon;
}
```

In the Codepen below, add the following classes and IDs to the HTML code:

- Class of `content` on all paragraphs before the first `h2`
- ID of `highlight` to the last `li` in the list
- Class of `team` on the `h3` and `p` elements between *About the Team* and *Our Values* (ie. lines 5-10)

Using those classes and IDs, make changes to the CSS so that:

- The `content` sections have bold text, and are purple (up to you what shade to choose).
- The `highlight` list item has a background colour, and is italicised.
- The `team` section has a different background colour to the list item, and has 20px of padding on the left and right sides.

{{< codepen id="vYypJLb" user="shecodesaus" title="CSS Selectors - Classes and IDs" >}}
