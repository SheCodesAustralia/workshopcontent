---
title: "Aside"
weight: 7
chapter: false
---

The `aside` element is for content that is related to the primary content of the webpage, but is not considered primary content itself.

We'll move our three images into an `aside`:

```diff
<main>
  <section>
    <h2>Anatomy and Physiology</h2>
    <h3>Size</h3>
    <p>The largest living species of turtle (and fourth-largest reptile) is the leatherback turtle which can reach over 2.7 m (8 ft 10 in) in length and weigh over 500 kg (1,100 lb).</p>
    <h3>Shell</h3>
    <p>The shell of a turtle is unique among vertebrates and serves to protect the animal and provide shelter from the elements.</p>
  </section>
  <section>
    <h2>Behaviour</h2>
    <h3>Diet and Feeding</h3>
    <p>Most turtle species are opportunistic omnivores; land-dwelling species are more herbivorous and aquatic ones more carnivorous.</p>
    <p>Turtles generally eat their food in a straightforward way, though some species have special feeding techniques.</p>
  </section>
+  <aside>
    <img src="http://localhost:1313/html_and_css/images/turtle_1.jpg"/>
    <img src="http://localhost:1313/html_and_css/images/turtle_2.jpg"/>
    <img src="http://localhost:1313/html_and_css/images/turtle_3.jpg"/>
+  </aside>
</main>
```

{{% notice test %}}

The three images will have a lighter background than the `main` and be on the right.

{{% /notice %}}

