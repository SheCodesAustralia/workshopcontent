---
title: "5. Fake it til you Bake it"
weight: 5
chapter: true
---

# Setting Up

We've got a website up and working - woohoo! We've got a few settings to play with, and then we can get some content loaded in.

After creating an application, we need to tell Django that it should use it. We do that in the file `bakery_project/settings.py`, open it in your code editor. We need to find `INSTALLED_APPS` and add a line containing `'{{APP_NAAME}}',` just above `]`. So the final product should look like this:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
+   'bakeries.apps.BakeriesConfig',

]
```


### Static and Media Files

We'll also need to add a path for static files. Go down to the *end* of the file, and just underneath the `STATIC_URL` entry, add a new one called `STATIC_ROOT`:

```python
+ STATICFILES_DIRS = [
+    BASE_DIR / "bakery_project" / "static",
+ ]

STATIC_URL = "static/"
+ STATIC_ROOT = BASE_DIR / "bakery_project" / "staticfiles"

+ MEDIA_URL = "media/"
+ MEDIA_ROOT = BASE_DIR / "bakery_project" / "media"

```
Don't forget to remove the + notations in your code, this is just telling you which lines are new.

#### Let’s break this down:

- **`STATICFILES_DIRS`**: Tells Django where to find your custom static files during development.  
  In this case, we’re keeping them inside `bakery_project/static/`.

- **`STATIC_URL`**: This is the URL prefix for accessing static files in your browser  
  (e.g., `http://localhost:8000/static/`).

- **`STATIC_ROOT`**: When you deploy your project, Django will collect all static files into this folder.  
  Think of this like a "ready-to-serve" folder for production.

- **`MEDIA_URL`**: This is the URL prefix for accessing media files  
  (e.g., `http://localhost:8000/media/`).

- **`MEDIA_ROOT`**: This tells Django where uploaded media files should be stored on your computer or server.

# Django Style

What's a template, you may ask?

A template is a file that we can re-use to present different information in a consistent format – for example, you could use a template to help you write a letter because although each letter might contain a different message and be addressed to a different person, they will share the same format.

A Django template's format is described in a language called HTML! If you have not already we recommend doing She Codes HTML/CSS tutorial! 

Before diving to create template, Let's make some changes in `bakery_project/settings.py`.

### Templates Directory

By default, Django already knows how to find templates stored inside each app folder. But as your project grows, it’s helpful to have a shared location where you keep your main templates.

Let’s tell Django to look inside a `templates` folder located at `bakery_project/templates/`. 

You don’t need to create the folder just yet, we’ll walk you through that later when we build your first template.

Open `settings.py`, and find the `TEMPLATES` section. Update the `'DIRS'` entry like this:

```

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
-        'DIRS': [],
+        'DIRS': [BASE_DIR / "bakery_project" / "templates"],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```


This tells Django to also search in this folder when rendering HTML pages.


{{% notice tip %}} Using a shared templates directory keeps things tidy, especially when building base layouts used across multiple apps. {{% /notice %}}

## Your first template!

Creating a template means creating a template file. Everything is a file, right? You have probably noticed this already.

Let’s create `templates` folder located at `bakery_project`. In our `templates` folder create a file and name it `index.html`.

Let's add a heading and some text! 

```
<h1>🧁 Bakery Finder</h1>

<div>
    <p>Need to find a bakery in a hurry? Here's a list of bakeries in your local area</p>
</div>

```
Don't forget to save! 

So how does your website look now? Visit it to find out: http://127.0.0.1:8000/ 

Huh, interesting, its still showing our Hello World! Remember earlier we wrote this in `views.py`?

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Welcome to our bakery.")

```

This is saying whenever we load our app show us Hello World. This is no longer helpful, as we want to show our lovely bakery app. Lets change that line starting with return to the below:

```python

return render(request, "index.html")

```
Now we are saying go find us `index.html` and show us that page. 

Save your code and refresh your website again and see how it looks.

## Let’s Add a Bit More Structure and Experiment with HTML Tags

We've written you some starter code to get you going, copy and paste the below into your index.html file, overriding what you added in earlier.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Bakery Finder</title>
  </head>
  <body>
    <header>
      <h1>🧁 Bakery Finder</h1>
    </header>

    <main>
      <p>Need to find a bakery in a hurry? Here's a list of bakeries in your local area:</p>
      
      <article>
        <h2>Sweet Treats</h2>
        <p class="description">Specializing in cupcakes and macarons 🍰</p>
        <p>Located at: 123 Tasty Street</p>
        <p>Rating ⭐: 4.8</p>
        <ul>
          <li>Chocolate Cupcake - $3.50</li>
          <li>Vanilla Macaron - $2.00</li>
        </ul>
      </article>

      <article>
        <h2>Bakehouse Delight</h2>
        <p class="description">Fresh croissants and artisan bread 🥐</p>
        <p>Located at: 456 Crusty Avenue</p>
        <p>Rating ⭐: 4.6</p>
        <ul>
          <li>Butter Croissant - $4.00</li>
          <li>Sourdough Loaf - $6.50</li>
        </ul>
      </article>
    </main>

    <footer>
      <p>© 2025 Bakery Finder</p>
    </footer>
  </body>
</html>
```

Now you can have a bit of a play, editing some of the items, what you page is called, whatever you like really!
As a reminder of some HTML tags, you might want to:

- Use `<h1>` to `<h6>` for headings.
- Wrap sections in `<article>`, `<main>`, and `<footer>` for structure.
- Use `<ul>` and `<li>` for lists of items (like baked goods!).
- Use `<p>` for text blocks.
- Add more `<article>` sections for new bakeries!

Go ahead and play around—change names, add new bakeries, change prices. This is your page!
