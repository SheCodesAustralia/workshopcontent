+++
title = "Post Types & Taxonomies"
weight = 3
chapter = true
+++

# The Post Type

WordPress is built on a database which contains a bunch of tables. One of the most important tables in the database looks something like this:

| post_ID | post_content | post_type | post_status |
| ---- | ----------- | ---------- | ---------- |
| 1 | \<!— wp:paragraph —> \<p>Welcome to WordPress. Thi... | post | publish |
| 2 | \<!— wp:paragraph —> \<p>This is an example page... | page | publish |
| 3 | \<!— wp:heading —> \<h2>Who we are</h2> | page | draft |

This is a simplified version but it does show you one of the most important things that you should understand if you want to really make the most of WordPress - content is stored in `posts` of different `post types` - and every WordPress site comes out of the box with two pre-made post types - One called `posts` and one called `pages`.

# Custom Post Types

We aren't limited to just Pages and Posts - we can do pretty much anything with WordPress by creating our own **Custom Post Types** and **Custom Fields**.

A great example of where custom post types might be used is a business that wants to create a profile page for each of their employees. They *could* do this using blog posts, but it would be messy and they would have to remember each time what layout and format they added for the other team member pages. A better way to do this would be to create a third post type - so instead of just pages & posts they would have pages, posts & team members. Team members might have their own special fields as well - like 'Position' or 'Hobbies.'
 
# Taxonomies

Posts & pages (and any other custom post types) are used for storing content. Tags & Categories are used to sort, order and categorise content. Categories & Tags are both examples of a **Taxonomy** - one hierarchical (categories) and one non-hierarchical (tags). As well as adding custom post types and custom fields, we can also add custom taxonomies in WordPress.

If we look at the example above (Team Members) we may want to organise those team members by Department, so that we can easily display an archive (list) page of all of the team members in that department.

We'll learn more about creating and using Custom Post Types, Custom Fields and Custom Taxonomies in the next section, Extending WordPress.
