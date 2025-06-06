---
title: "6. She's a Model"
weight: 6
chapter: true
---
So we've got a page but its all hardcoded and manual. That's no fun, we want dynamic data. Let's start by getting ourselves a database to store that data in.

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

To create a database for our app, let's run the following in the console: `python manage.py migrate` (we need to be in the `bakery_site` directory that contains the `manage.py` file). If your server is still running, press Control + C to stop it to run the next command.

If that goes well, you should see something like this:

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

And we're done! Time to start the web server and see if our website is working! See if you remember it from earlier...


## Django Models

What we want to create is something that will store all the details about local bakeries and their scrumptious offerings in our bakery_project app. But to be able to do that, we need to talk a little bit about a concept in programming called `objects`.


### Objects

In programming, there’s a powerful concept called object-oriented programming. Instead of writing a long list of instructions, we can structure our code to model real-world things and how they interact — just like objects in real life.

So, what is an object? Think of it as a bundle of properties (descriptions) and actions (things it can do). 

We want to build something that helps people discover amazing local bakeries and their delicious treats.

To do that, we need to model our world using objects:

What are the key properties of a Bakery?

What is a BakeryItem, and what should it include?

Let’s start thinking like object-oriented programmers:
What data do we need to describe a bakery or a baked good?
What actions might they have?

For example, a Bakery should have:

```
Bakery
-------
name: The bakery's name.
address: Where the bakery is located.
cuisine: The type of baked goods or specialties it offers.
rating: A rating to help users gauge quality.
image: An optional image URL representing the bakery.
```

And an Item produced by the bakery should include:

```
Item
-------
bakery: A reference to the bakery it belongs to.
name: The name of the baked good (like "Chocolate Croissant" or "Sourdough Bread").
price: How much the item costs.
image: An optional image URL of the item.
```

What kind of things could be done with these models? It would be very useful to have a method that returns a human-readable description of each instance. In Django, this is typically done using the `__str__` method. By defining this method, you ensure that when a Bakery or Item object is converted to a string, it provides a clear and concise representation (usually the name).

Let's start modeling it in Django!


## Building out our models

Now that we understand what an object is, we can use that knowledge to create a Django model for our bakery and another for its items.

In Django, a model is a special type of object that gets saved to a 'database'. A database is simply a structured collection of data — it’s where you’ll store information about users, bakeries, their baked goods, and more.

For this project, we’ll be using a SQLite database, which is Django’s default option. It’s lightweight and perfect for what we need right now.

You can imagine a model like a spreadsheet:

The columns represent the fields or attributes (like name, price, or location),

And each row is a single record — one bakery, one item, etc.

Each model in Django becomes a table in the database, and the cool part is: models can be connected to each other! So a bakery can have many bakery items, and each item can belong to a specific bakery.



### Creating a Bakery model

In the `bakeries/models.py` file we define all objects called `Models` – this is a place in which we will define our bakery data models.

Let's open `bakeries/models.py` in the code editor, remove everything from it, and write code like this:

```python

from django.db import models


class Bakery(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    cuisine = models.CharField(max_length=255)
    rating = models.IntegerField()
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


```
{{% notice info %}}  

Double-check that you use two underscore characters (`_`) on each side of `str`. This convention is used frequently in Python and they have a fun name "dunder" (short for "double-underscore").

{{% /notice %}}


Let's break that down a bit.

The line starting with `from` or `import` is a line that add some bits from other files. So instead of copying and pasting the same things in every file, we can include some parts with `from ... import ...`.

`class Bakery(models.Model)` – this line defines our model (it is an `object`).
- `class` is a special keyword that indicates that we are defining an object.
- `Bakery` is the name of our model. We can give it a different name (but we must avoid special characters and whitespace). Always start a class name with an uppercase letter.
- `models.Model` means that the Bakery is a Django Model, so Django knows that it should be saved in the database.

Now we define the properties we were talking about: `name`, `address`, `cuisine`, `rating` and `image`. To do that we need to define the type of each field (Is it text? A number? A date? A relation to another object, like a User?)

- `models.CharField` – this is how you define text with a limited number of characters.
- `models.TextField` – this is for long text without a limit. Sounds ideal for address content, right?
- `models.IntegerField` – this is for storing whole numbers.
- `models.URLField` – this is for storing image URLs.

Methods often `return` something. There is an example of that in the `__str__` method. In this scenario, when we call `__str__()` we will get a text (**string**) with a Bakery name.

Also notice `def __str__(self):` is indented. Because Python is sensitive to whitespace, we need to indent our methods inside the class. Otherwise, the methods won't belong to the class, and you can get some unexpected behavior.

If you are curious about the rest of built-in Django from what we've done so far, have a look at Django's [documentation](https://docs.djangoproject.com/en/5.1/ref/models/fields/#field-types).

### Creating an Item model

Now let's define our `Item` model, which represents the baked goods offered by each bakery. Just below your Bakery model (at the very bottom of your code) in `bakeries/models.py` file, add the following code:


```python

class Item(models.Model):
    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.URLField(null=True, blank=True)

    def __str__(self):
       return self.name

```

When we write: class Item(models.Model) we’re defining a model called Item. This is how we tell Django: "Hey, I want to create something called an Item and store it in the database."

The bit in brackets - models.Model – means that Item is inheriting from Django’s built-in Model class. That’s just a fancy way of saying:
“Make this a Django model with all the features needed to connect to the database.”

Thanks to this, Django knows to create a database table for Item. Each time we create a new item (like a croissant or cupcake), Django will save it as a row in the Item table.

So if you’ve already created a model for your Bakery as well, you now have two tables in your database:

One for `Bakery`

One for `Item`

Each model = one table. Each instance (object) = one row.

We just defined the properties of an `Item` such as: `bakery`, `name`, `price` and `image`. To do that we defined the type of each field (Is it text? A number? A relation to another object?). This is exactly the same way we made our `Bakery` model.

Let's find out what's new here.

- `models.ForeignKey(Bakery, on_delete=models.CASCADE)` – This field creates a relationship between each Item and a Bakery. The on_delete=models.CASCADE argument means that if a bakery is deleted, all associated items will also be removed from the database. That makes sense, we wouldn't want to find the croissant of our dreams only to find out that bakery closed down in 2003!
- `models.FloatField` – This field stores the price of the item as a floating-point number, allowing for decimals. This way our data will show up in dollars and cents, like we might be used to seeing at shops.

We are using a `__str__` method again. In this scenario, when we call `__str__()` we will get a text (**string**) with an Item name.

If something is still not clear about models, feel free to ask one of the mentors! Spot the purple shirt? Hands up now! We know its a lot to take in but you should be super proud of yourself. Hopefully it looks slightly less magic for you now.


## Create tables for models in your database

The last step here is to add our new models to our database. First we have to make Django know that we have some changes in our models (we have just created it!). Go to your console window and type `python manage.py makemigrations bakeries`. It will look like this:

```
(myvenv) bakery_site% python manage.py makemigrations bakeries
Migrations for 'bakeries':
  bakeries/migrations/0001_initial.py
    + Create model Bakery
    + Create model Item
```
{{% notice info %}}  

**Note:** Remember to save the files you edit. Otherwise, your computer will execute the previous version which might give you unexpected error messages.

{{% /notice %}}

Django prepared a migration file for us that we now have to apply to our database. Type `python manage.py migrate bakeries` and the output should be as follows:

```
(myvenv) ~/bakery_site$ python manage.py migrate bakeries
Operations to perform:
  Apply all migrations: bakeries
Running migrations:
  Applying bakeries.0001_initial... OK
```

Hurray! Our models are now in our database! It would be nice to see it, right? Jump to the next chapter to see what your models looks like!
