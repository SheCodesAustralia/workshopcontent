

Let's make some changes in `bakery_project/settings.py`. Open the file using the code editor you installed earlier.

### Templates Directory

By default, Django already knows how to find templates stored inside each app folder. But as your project grows, it’s helpful to have a shared location where you keep your main templates.

Let’s tell Django to look inside a `templates` folder located at `bakery_project/templates/`.

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

You don’t need to create the folder just yet — we’ll walk you through that later when we build your first template.

{{% notice tip %}} Using a shared templates directory keeps things tidy, especially when building base layouts used across multiple apps. {{% /notice %}}