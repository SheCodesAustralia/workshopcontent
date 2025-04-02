# Installation
In this tutorial you will be building a Bakery app. In order to do that, as you go through the tutorial you'll be instructed on how to
install various software on your computer and set up some online accounts as needed (if you are using local desktop environment) or instructed on how to create online accounts only (if you are using cloud development). This page gathers all of the installation and sign-up instructions in one place .

# Chromebook Installation
To set up your Chromebook, follow the instructions below:

## Using a Cloud IDE Environment (Recommended for Chromebook or Low-Memory Devices)

For users on Chromebooks or laptops with limited memory, we recommend using a **cloud IDE environment**. This allows you to interact with the command line, Python, and Django directly through your browser, with a code editor already installed.

Your installation experience may differ slightly depending on the environment.

---

## Step 1: Create a GitHub Account (if you already don't have one)

1. Go to [GitHub.com](https://github.com) and sign up for a **free** user account.
2. Remember your password — consider saving it in a password manager if you use one.

---

## Step 2: Create a GitHub Project

1. Visit [this link](https://github.com/new) to create a new repository.
2. Use **`bakery_app`** as the project name.
3. Set the repository to **Public** (this is required for deployment; you can make it private later).
4. In Initialize this repository with, make sure to:
   - Add a **README.md** file.
   - Add a **.gitignore** file and select Python.

## Step 3:  Start a Codespace

If you don't want to install any app in your laptop, you can install Codespaces. To install Codespaces

1. Go to GitHub [Codespaces](https://github.com/codespaces/new) and select the repository you just created. Click 'Create Codespace'

![Screenshot of codespace.](../images/codespace.png)

wait a little bit and you will see something like that

The [VSCode] (https://code.visualstudio.com/docs/?dv=win64user) editor will open for you automatically.
If you see a notification that says "Install Python", please click on it. If not prompted, click the "Extensions" icon on the left sidebar in the Codespace editor. Search for "Python" and click "Install."

![Screenshot of codespace python.](../images/codespace_python.png)

The bash terminal(similar to Linus) is at the bottom page.

![Screenshot of codespace terminal.](../images/codespace_terminal.png)

By default, the GitHub Codespace environment will be deleted after 1 month (this applies only to the environment, not your code). To prevent auto-deletion, you can adjust the settings on the page: https://github.com/codespaces

![Screenshot of codespace-auto-delete-off.](../images/codespace-auto-delete-off.png)

## Step 4: Continue with the Tutorial.
Follow the next steps from the section Set up a virtual environment and install Django.
Follow than sections for Ubuntu/Linux. Use the Codespaces command line (terminal), accessible through your browser.

<!--endsec-->


# macOS, Windows, Linux Installation {#macos-windows-linux}
If you are not using a Chromebook, your experience will be a little different as you need to download and install some software locally as well as set up online accounts.

To install software on your machine, follow the instructions below:

## Brief intro to the command line {#intro-command-line}
Many of the steps below reference the "console", "terminal", "command window", or "command line" -- these all mean the same thing: a window on your computer where you can enter commands. When you get to the main tutorial, you'll learn more about the command line. For now, the main thing you need to know is how to open a command window and what it looks like:

Opening:macOS
Go to Launchpad --> Other -->Terminal

Opening: Linux
It's probably under applications --> Acessories --> Terminal, or Applications --> System --> Terminal, but that may depend on your system. If It's not there, you can try to Google it.

Opening: Windows

Depending on your version of Windows and your keyboard, one of the following should open a command window (you may have to experiment a bit, but you don't have to try all of these suggestions):

* Go to the Start menu or screen, and enter "Command Prompt" in the search field.
* Go to Start menu → Windows System → Command Prompt.
* Go to Start menu → All Programs → Accessories → Command Prompt.
* Go to the Start screen, hover your mouse in the lower-left corner of the screen, and click the down arrow that appears (on a touch screen, instead flick up from the bottom of the screen). The Apps page should open. Click on Command Prompt in the Windows System section.
* Hold the special Windows key on your keyboard and press the "X" key. Choose "Command Prompt" from the pop-up menu.
* Hold the Windows key and press the "R" key to get a "Run" window. Type "cmd" in the box, and click the OK key.

![Screenshot of windows-plus-r.](images/windows-plus-r.png)

Later in this tutorial, you will need to have two command windows open at the same time. However, on some versions of Windows, if you already have one command window open and you try to open a second one using the same method, it will instead point you to the command window you already have open. Try it now on your computer and see what happens! If you only get one command window, try one of the other methods in the list above. At least one of them should result in a new command window being opened.

## Install Python {#python}
{% include "/python_installation/instructions.md" %}

## Install a code editor {#code-editor}

There are a lot of different editors and it largely boils down to personal preference. Most Python programmers use complex but extremely powerful IDEs (Integrated Development Environments), such as PyCharm. As a beginner, however, that's probably less suitable; our recommendations are equally powerful, but a lot simpler.

Our suggestions are below, but feel free to ask your coach what their preferences are – it'll be easier to get help from them.

## Set up virtualenv and install Django {#virtualenv}
{% include "/django_installation/instructions.md" %}

## Install Git {#git}
{% include "/deploy/install_git.md" %}

## Create a GitHub account {#github-account}
Go to [GitHub.com](https://www.github.com) and sign up for a new, free user account. Be sure to remember your password (add it to your password manager, if you use one).

## Create a PythonAnywhere account {#pythonanywhere-account}
{% include "/deploy/signup_pythonanywhere.md" %}


# Start reading

Congratulations, you are all set up and ready to go! If you still have some time before the workshop, it would be useful to start reading a few of the beginning chapters:

* [How the internet works](../how_the_internet_works/README.md)

* [Introduction to the command line](../intro_to_command_line/README.md)

* [Introduction to Python](../python_introduction/README.md)

* [What is Django?](../django/README.md)


# Enjoy the workshop!

When you begin the workshop, you'll be able to go straight to [Your first Django project!](../django_start_project/README.md) because you already covered the material in the earlier chapters.
