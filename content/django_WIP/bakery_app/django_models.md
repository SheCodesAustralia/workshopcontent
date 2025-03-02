<!--

- **Updating the Names:**  
  
Change **{{APP_NAME}}** to your final app name. All instances of **{{APP_NAME}}** in the text will then reflect this new name.( on 25/2/25 based on code repo
{{APP_NAME}} : bakeries )

same with:

{{PROJECT_DIRECTORY}}

{{PROJECT_NAME}} : bakery_project



-->
Ready for the content of our personalised letter? Let's make it happen! 

# Django models

What we want to create is something that will store all the details about local bakeries and their scrumptious offerings in our {{app_name}} app. But to be able to do that, we need to talk a little bit about a concept in programming called `objects`.


## Objects

There is a concept in programming called `object-oriented programming`. The idea is that instead of writing everything as a boring sequence of programming instructions, we can model things and define how they interact with each other.

So what is an object? It is a collection of properties and actions. It sounds weird, but we will give you an example.

If we want to model a cat, we will create an object `Cat` that has some properties such as `color`, `age`, `mood` (like good, bad, or sleepy ;)), and `owner` (which could be assigned a `Person` object – or maybe, in case of a stray cat, this property could be empty).

Then the `Cat` has some actions: `purr`, `scratch`, or `feed` (in which case, we will give the cat some `CatFood`, which could be a separate object with properties, like `taste`).

```
Cat
--------
color
age
mood
owner
purr()
scratch()
feed(cat_food)
```

```
CatFood
--------
taste
```

So basically the idea is to describe real things in code with properties (called `object properties`) and actions (called `methods`).

How will we model our bakery items and bakeries then? We want to build a bakery app that helps users discover the best local bakeries and their delectable offerings, right?

We need to answer the question: what `object properties` do we need for a bakery? What is a bakery item? What properties should it have? 

For example, a Bakery should have:

name: The bakery's name.
address: Where the bakery is located.
cuisine: The type of baked goods or specialties it offers.
rating: A rating to help users gauge quality.
image: An optional image URL representing the bakery.


And an Item produced by the bakery should include:

bakery: A reference to the bakery it belongs to.
name: The name of the baked good (like "Chocolate Croissant" or "Sourdough Bread").
price: How much the item costs.
image: An optional image URL of the item.


What kind of things could be done with these models? It would be very useful to have a method that returns a human-readable description of each instance. In Django, this is typically done using the `__str__` method. By defining this method, you ensure that when a Bakery or Item object is converted to a string, it provides a clear and concise representation (usually the name).

Since we already know what we want to achieve, let's start modeling it in Django!


## Django model

Knowing what an object is, we can create a Django model for our bakery and a model for its items.

A model in Django is a special kind of object – it is saved in the `database`. A database is a collection of data. This is a place in which you will store information about users, your bakeries, their items, etc. We will be using a SQLite database to store our data. This is the default Django database adapter – it'll be enough for us right now.

You can think of a model in the database as a spreadsheet with columns (fields) and rows (data). Each model will represent a table on our database and it can interact with other tables! 

### Creating an application

To keep everything tidy, we will create a separate application inside our project. It is very nice to have everything organized from the very beginning. To create an application we need to run the following command in the console (from `{{PROJECT_DIRECTORY}}` directory where `manage.py` file is):

```
(myvenv) {{PROJECT_DIRECTORY}}% python manage.py startapp {{APP_NAME}}
```

```
(myvenv) C:\Users\Name\{{PROJECT_DIRECTORY}}> python manage.py startapp {{APP_NAME}}
```

You will notice that a new `{{APP_NAME}}` directory is created and it contains a number of files now. The directories and files in our project should look like this:

```
{{PROJECT_DIRECTORY}}
├── {{APP_NAME}}
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── {{PROJECT_NAME}}
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myvenv
│   └── ...
└── requirements.txt

```

After creating an application, we also need to tell Django that it should use it. We do that in the file `{{PROJECT_NAME}}/settings.py`, open it in your code editor. We need to find `INSTALLED_APPS` and add a line containing `'{{APP_NAAME}}',` just above `]`. So the final product should look like this:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
+   '{{APP_NAME}}',
]
```

### Creating a Bakery model

In the `{{APP_NAME}}/models.py` file we define all objects called `Models` – this is a place in which we will define our bakery data models.

Let's open `{{APP_NAME}}/models.py` in the code editor, remove everything from it, and write code like this:

```python

+from django.db import models


+class Bakery(models.Model):
+    name = models.CharField(max_length=255)
+    address = models.TextField()
+    cuisine = models.CharField(max_length=255)
+    rating = models.IntegerField()
+    image = models.URLField(null=True, blank=True)
+
+    def __str__(self):
+        return self.name


```
{{% notice info %}}  

Double-check that you use two underscore characters (`_`) on each side of `str`. This convention is used frequently in Python and sometimes we also call them "dunder" (short for "double-underscore").

{{% /notice %}}


It looks scary, right? But don't worry – we will explain what these lines mean!

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


We will not explain every bit of code here since it would take too much time. You should take a look at Django's documentation if you want to know more about Model fields and how to define things other than those described above (https://docs.djangoproject.com/en/5.1/ref/models/fields/#field-types).


Methods often `return` something. There is an example of that in the `__str__` method. In this scenario, when we call `__str__()` we will get a text (**string**) with a Bakery name.

Also notice `def __str__(self):` is indented inside our class. Because Python is sensitive to whitespace, we need to indent our methods inside the class. Otherwise, the methods won't belong to the class, and you can get some unexpected behavior.


### Creating an Item model

Now let's define our `Item` model, which represents the baked goods offered by each bakery. Just below your Bakery modelin `{{APP_NAME}}/models.py` file, add the following code:


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

+class Item(models.Model):
+    bakery = models.ForeignKey(Bakery, on_delete=models.CASCADE)
+    name = models.CharField(max_length=255)
+    price = models.FloatField()
+    image = models.URLField(null=True, blank=True)

+    def __str__(self):
+       return self.name

```


`class Item(models.Model)` defines our Item model, which inherits from Django’s base Model class. This tells Django to save instances of Item in the database as a table. So far we have two tables! `Bakery` and `Item`.

We just defined the properties of an `Item` such as: `bakery`, `name`, `price` and `image`. To do that we need to define the type of each field! (Is it A text? A number? A relation to another object?) Exactly the same we took care of our `Bakery` model.

I bet it looks less scary, right? Let's find out what is new here? 

- `models.ForeignKey(Bakery, on_delete=models.CASCADE)` – This field creates a relationship between each Item and a Bakery. The on_delete=models.CASCADE argument means that if a bakery is deleted, all associated items will also be removed from the database.
- `models.FloatField` – This field stores the price of the item as a floating-point number, allowing for decimals.

We have the same method `__str__`. In this scenario, when we call `__str__()` we will get a text (**string**) with an Item name.

If something is still not clear about models, feel free to ask one of the mentors! Spot the purple shirt? hands up now! We know it is complicated, especially when you learn what objects and functions are at the same time. But hopefully it looks slightly less magic for you now!


### Create tables for models in your database

The last step here is to add our new models to our database. First we have to make Django know that we have some changes in our models. (We have just created it!) Go to your console window and type `python manage.py makemigrations {{APP_NAME}}`. It will look like this:

```
(myvenv) {{PROJECT_DIRECTORY}}% python manage.py makemigrations {{APP_NAME}}
Migrations for '{{APP_NAME}}':
  {{APP_NAME}}/migrations/0001_initial.py
    + Create model Bakery
    + Create model Item
```
{{% notice info %}}  

**Note:** Remember to save the files you edit. Otherwise, your computer will execute the previous version which might give you unexpected error messages.

{{% /notice %}}

Django prepared a migration file for us that we now have to apply to our database. Type `python manage.py migrate {{APP_NAME}}` and the output should be as follows:

```
(myvenv) ~/{{PROJECT_DIRECTORY}}$ python manage.py migrate {{APP_NAME}}
Operations to perform:
  Apply all migrations: {{APP_NAME}}
Running migrations:
  Applying {{APP_NAME}}.0001_initial... OK
```

Hurray! Our models are now in our database! It would be nice to see it, right? Jump to the next chapter to see what your models looks like!
