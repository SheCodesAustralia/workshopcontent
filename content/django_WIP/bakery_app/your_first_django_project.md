
<!--

### How to Use This Template

- **Updating the App Name:**  
  Change the `app_name` value in the front matter to your final app name. All instances of `{{ app_name }}` in the text will then reflect this new name.

- **Changing the Project Directory:**  
  Similarly, update the `project_slug` variable if you decide on a different directory name. This variable is used in command-line examples to help maintain consistency.

This approach makes your instructions scalable and easy to update without having to search and replace every occurrence manually.

-->
---
app_name: Bakery Finder
project_slug: bakeryfinder
djangoinstallation_link: /tutorial/django-installation
virtualenv_link: /tutorial/working-with-virtualenv
---

## What will you learn during the tutorial?

By the end of this tutorial, you'll have built a fully functional Django application that showcases a **{{ site.app_name }}** app for discovering the best local bakeries and their delicious offerings—all at your fingertips.

You’ll learn how to structure your project with Django’s models, views, and templates, and you'll add the finishing touches with custom styling to make your site visually appealing. We’ll even guide you through deploying your app online so that everyone can explore your bakeries and their offerings!

It will (more or less) look like this:

![Figure 1.1](images/placeholder.png ) 



# Your first Django project!

The first step is to create our **{{ site.app_name }}** app is to start a new Django project. Basically, this means that we'll run some scripts provided by Django that will create the skeleton of a Django project for us. This is just a bunch of directories and files that we will use later.

The names of some files and directories are very important for Django. You should not rename the files that we are about to create. Moving them to a different place is also not a good idea. Django needs to maintain a certain structure to be able to find important things.



> Remember to run everything in the virtualenv. If you don't see a prefix `(myvenv)` in your console, you need to activate your virtualenv. We explained how to do that in the [Django installation]({{ site.djangoinstallation_link }}) chapter in the [Working with virtualenv]({{ site.virtualenv_link }}) part. Typing `myvenv\Scripts\activate` on Windows or
`source myvenv/bin/activate` on macOS or Linux will do this for you.

<!--sec data-title="Create project: macOS or Linux" data-id="django_start_project_OSX_Linux" data-collapse=true ces-->

In your macOS or Linux console, you should run the following command. **Don't forget to add the period (or dot) `.` at the end!**

{% filename %}command-line{% endfilename %}
```
(myvenv) ~/{{ project_slug }}$ django-admin startproject mysite .
```



> The period `.` is crucial because it tells the script to install Django in your current directory (for which the period `.` is a short-hand reference).

> **Note** When typing the command above, remember that you only type the part which starts by `django-admin`.
The `(myvenv) ~/{{ project_slug }}$` part shown here is just example of the prompt that will be inviting your input on your command line.

<!--endsec-->

<!--sec data-title="Create project: Windows" data-id="django_start_project_windows" data-collapse=true ces-->






