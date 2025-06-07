---
title: "2. Installation"
weight: 2
chapter: true
---

# Installation

In this tutorial you will be building a Bakery app. In order to do that, as you go through the tutorial you'll be instructed on how to install various software on your computer and set up some online accounts as needed if you wish to put your site live on the internet.

---

### Brief intro to the command line

Many of the steps below reference the `console`, `terminal`, `command window`, or `command line` -- these all mean the same thing: a window on your computer where you can enter commands. For now, the main thing you need to know is how to open a command window and what it looks like:

#### Opening the command line

- **macOS:** Go to **Launchpad → Other → Terminal**.
- **Linux:** Usually found under **Applications → Accessories → Terminal**.
- **Windows:** 
  - Search **Command Prompt** in the Start menu.
  - Open **Windows System → Command Prompt**.
  - Use `Win + R`, type `cmd`, and press Enter.

#### Install Python

Django is written in Python. We need Python to do anything in Django. Let's start by installing it! We want you to install the latest version of Python 3, so if you have any earlier version, you will need to upgrade it. If you already have version 3.10 or higher you should be fine.

##### **Windows**

1. Download **Python** from [python.org](https://www.python.org/downloads/windows/).
2. Run the installer and ensure you **tick "Add Python 3 to PATH"** before installing.

##### **macOS**
1. Go to [python.org](https://www.python.org/downloads/).
2. Download the latest **Python 3.x** installer.
3. Run the installer and follow the instructions.

##### **Linux**
Check if Python is installed:

```sh
python3 --version
```

If not, install it based on your Linux distribution. What's a Linux distribution? Distributions are packaged collections of software built on top of the Linux kernel, offering a complete operating system experience. We've pulled out a couple to get you started, if yours isn't there - Google is your friend, or ask a mentor for help.

```sh
sudo apt install python3   # Debian/Ubuntu
sudo dnf install python3   # Fedora
sudo zypper install python3  # openSUSE
```

### Install a Code Editor

There are a lot of different editors and it largely boils down to personal preference. Most Python programmers use complex but extremely powerful IDEs (Integrated Development Environments), such as PyCharm. As a beginner, however, that's probably less suitable; our recommendations are equally powerful, but a lot simpler:

- [Visual Studio Code](https://code.visualstudio.com/)

#### Why are we installing a code editor?

You might be wondering why we are installing this special code editor software, rather than using something like Word or Notepad.

The first reason is that code needs to be plain text, and the problem with programs like Word and Textedit is that they don't actually produce plain text, they produce rich text (with fonts and formatting), using custom formats like RTF (Rich Text Format).

The second reason is that code editors are specialized for editing code, so they can provide helpful features like highlighting code with color according to its meaning, or automatically closing quotes for you.

We'll see all this in action later. Soon, you'll come to think of your trusty old code editor as one of your favorite tools. 

### Set up virtual environment and install Django

Before we install Django we will get you to install an extremely useful tool to help keep your coding environment tidy on your computer. It's possible to skip this step, but it's highly recommended to follow it. Starting with the best possible setup will save you a lot of trouble in the future!

So, let's create a virtual environment (also called a virtualenv). Virtualenv will isolate your Python/Django setup on a per-project basis. This means that any changes you make to one website won't affect any others you're also developing. Neat, right?

All you need to do is find a directory in which you want to create the virtualenv; your home directory, for example. On Windows, it might look like `C:\Users\Name\` (where Name is the name of your login).


#### Create a virtual environment

For this tutorial we will be using a new directory bakery_site from your home directory:

```sh
mkdir bakery_site
cd bakery_site
```

We will make a virtualenv called `myvenv`. The general command will be in the format:

**Windows:**

```sh
python -m venv myvenv
```

**MacOS/Linux:**

```sh
python3 -m venv myvenv
```

Where myvenv is the name of your virtualenv. You can use any other name, but stick to lowercase and use no spaces, accents or special characters. It is also a good idea to keep the name short – you'll be referencing it a lot!


#### Working with virtualenv

The command above will create a directory called myvenv (or whatever name you chose) that contains our virtual environment (basically a bunch of directories and files).

Start your virtual environment by running:

**Windows:**

```sh
myvenv\Scripts\activate
```

**MacOS/Linux:**

```sh
source myvenv/bin/activate
```

#### Install Django

OK, we have all important dependencies in place. We can finally install Django!

Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:

1. Ensure you have the latest **pip**:

```sh
pip install --upgrade pip
```

2. Find your `bakery_site` folder on your device and open it in VS Code. Create a `requirements.txt` file and add:

```
Django~=5.1.2
```
Hit save, and head back to your terminal.

3. Install dependencies:

```sh
pip install -r requirements.txt
```
This is telling your machine to go and look at the requirements file we just created and install the things created within. If you're having any issues with this step, grab a mentor.