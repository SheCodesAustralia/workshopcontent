---
title: "3. Your First Django Project"
weight: 3
chapter: true
---

# Your first Django project!


{{% notice info %}}  

Steps of instruction for this chapter is based on tutorials by Django Girls (https://github.com/DjangoGirls/tutorial).

{{% /notice %}}


# Your first Django project!

The first step is to create our Bakery Finder app is to start a new Django project. Django has some ~magic~ meaning that went we run some scripts, Django will create the skeleton of a Django project for us! The skeleton is a bunch of files that we will explain as we go.

Naming of these files and directories are very important. Django needs to maintain a certain structure to be able to find important bits of information. If they are renamed or moved, it might get confused or throw some unexpected errors. As such, you shouldn't rename the files that we are about to create, or move them around.

Ready to get going?


{{% notice note %}}

Remember to run everything in the virtualenv. If you don't see a prefix `(myvenv)` in your console, you need to activate your virtualenv. We explained how to do that in the [Django installation](<<DJANGO_INSTALLATION_LINK>>) chapter in the [Working with virtualenv](<<VIRTUALENV_LINK>>) part. Typing `myvenv\Scripts\activate` on Windows or
`source myvenv/bin/activate` on macOS or Linux will do this for you.

{{% /notice %}}

## Create Project


### Mac/Linux Users:

In your macOS or Linux console, run the following command. Don’t forget to add the period (or dot) `.` at the end! The period `.` is essential because it tells the script to install Django in your current directory (fun fact: the period `.` is a short-hand reference).

```
(myvenv) bakery_site% django-admin startproject bakery_project .
```

{{% notice note %}}

When typing the command above, remember that you only type the part which starts with django-admin. The `(myvenv) ~/bakery_site$` part shown here is just example of what your command line will be showing, waiting for your instructions. Yours may look different if your file is called something different or based on the settings on your device. If you're unsure - check in with a mentor!

{{% /notice %}}



### Windows Users:

On your Windows terminal, run the following command. Don’t forget to add the period (or dot) `.` at the end! The period `.` is essential because it tells the script to install Django in your current directory (fun fact: the period `.` is a short-hand reference).

```
(myvenv) C:\Users\Name\bakery_site django-admin.exe startproject bakery_project .
```

{{% notice note %}}

**Note** When typing the command above, remember that you only type the part which starts by `django-admin.exe`.
The `(myvenv) C:\Users\Name\bakery_site` part shown here is just example of what your command line will be showing, waiting for your instructions. Yours may look different if your file is called something different or based on the settings on your device. If you're unsure - check in with a mentor!

{{% /notice %}}




## Understanding Your Project Structure


`django-admin.py` is a script that will create the directories and files for you. You should now have a directory structure which looks like this:

```
bakery_site
├── manage.py
├── bakery_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myvenv
│   └── ...
└── requirements.txt
```


{{% notice note %}}

In your directory structure, you will also see your `myvenv` directory that we created before.

{{% /notice %}}

Lets walk through what some of these files are.

The `manage.py` is a script that helps with management of the site. One of the things this file lets us do is to start a web server on our computer without installing anything else.

The `settings.py` file contains the configuration of your website, much like your settings app on your phone or laptop.

Remember when we talked about letters earlier? The `urls.py` file is like an address book, so we can write different letters to different people, with personalised content. There's a little thing called the 'urlresolver' that's going to help us with that down the track.

We can ignore the other files for now as we won't change them - the only thing to remember is not to delete them by accident!




<!--  
In the `bakery_app` so far( 24/02/25), the `settings.py` file remains unchanged from the default, except for the part where we need to add our app to the `INSTALLED_APPS` list—which is not required at this stage! 

The Django Girls tutorial provides explanations about different parts of `settings.py` that can be modified. This is helpful for giving users a broader understanding of what the settings file includes.  

If we need a shorter version of tutorial some parts of this section are unnecessary 
-->



## Changing settings

Let's make some changes in `bakery_project/settings.py`. Open the file using the code editor you installed earlier.

<!-- my personal opinion: this note on how to open the file is unnecessary as we expect the user be already on vscode, PLEASE FEEL FREE TO SKIP THIS **Note** if required-->

{{% notice note %}}

**Note**: Keep in mind that `settings.py` is a regular file, like any other. You can open it from inside the code editor, using the "File -> Open" menu action. This should get you the usual window in which you can navigate to your `settings.py` file and select it. Alternatively, you can open the file by navigating to the `bakery_site/bakery_project` folder on your desktop and right-clicking on it. Then, select your code editor from the list.

{{% /notice %}}


### Time Zone and Location

Having the correct time on our website will be important to make sure the bakeries are open! We've included the timezone for Perth below, but feelf free to check out [Wikipedia's list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) and copy your relevant time zone.

In `settings.py`, find the line that contains `TIME_ZONE` and change it to your timezone.  For example:

```python
-TIME_ZONE = "UTC"
+TIME_ZONE = 'Australia/Perth'
```
We also probably want to make sure our website is in the correct language so our pastry-loving customers can find us! Lets have a look at the `language code`. A `language code` has two parts - one is the language e.g. `en` for English or `de` for German - and the second part is the country code e.g. `de` for Germany or `AU` for Australia. This could be important for say British English vs American English. 

Let's update the default US English to Australian English by changing this line:

```python
-LANGUAGE_CODE = "en-us"
+LANGUAGE_CODE = 'en-AU'
```



### Static and Media Files

We'll also need to add a path for static files. (We'll find out all about static files and CSS later in the tutorial.) Go down to the *end* of the file, and just underneath the `STATIC_URL` entry, add a new one called `STATIC_ROOT`:

```
+STATICFILES_DIRS = [
+    BASE_DIR / "bakery_project" / "static",
+]

STATIC_URL = "static/"
+STATIC_ROOT = BASE_DIR / "bakery_project" / "staticfiles"

+MEDIA_URL = "media/"
+MEDIA_ROOT = BASE_DIR / "bakery_project" / "media"

```

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

You don’t need to create these folders just yet — Django will take care of it when we use the `collectstatic` command or when users upload media.

{{% notice tip %}}  
**Tip**: You might not use media files right away, but it’s good practice to include the setup early.  
That way you’re ready when you add delicious cupcake photos later!  
{{% /notice %}}

## Set up a database

There's a lot of different database software that can store data for your site. We'll use the default one, `sqlite3`.

This is already set up in this part of your `mysite/settings.py` file:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

To create a database for our app, let's run the following in the console: `python manage.py migrate` (we need to be in the `bakery_site` directory that contains the `manage.py` file). If that goes well, you should see something like this:

```

(myvenv)  bakery_site% python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

And we're done! Time to start the web server and see if our website is working!

## Starting the web server

You need to be in the directory that contains the `manage.py` file (the `bakery_site` directory). In the console, we can start the web server by running `python manage.py runserver`:

```
(myvenv) bakery_site% python manage.py runserver
```

If you are on a Chromebook, use this command instead:

```
(myvenv) bakery_site% python manage.py runserver 0.0.0.0:8080
```


If you are on Windows and this fails with `UnicodeDecodeError`, use this command instead:

```
(myvenv) bakery_site% python manage.py runserver 0:8000
```


Now you need to check that your website is running. Open your browser ( eg Firefox, Chrome, Safari etc) and enter this address:

```
http://127.0.0.1:8000/
```

You can open this in another browser window and you should see the Django install worked page.

Congratulations! You've just created your first website and run it using a web server! Isn't that awesome?

![Install worked!](images/install_worked.png)

Note that a command window can only run one thing at a time, and the command window you opened earlier is running the web server. As long as the web server is running and waiting for additional incoming requests, the terminal will accept new text but will not execute new commands.

To type additional commands while the web server is running, open a new terminal window and activate your virtualenv. To stop the web server, switch back to the window in which it's running and press CTRL+C - Control and C keys together (on Windows, you might have to press Ctrl+Break).



Ready for the next step? It's time to create some content!

