+++
title = "Python installation"
date = 2021-02-04T20:02:00+08:00
weight = 10
chapter = true
pre = "<b>1. </b>"
+++

# Let’s start with Python

We're finally here!

We need Python before we can start. If you don't have Python installed yet, start by installing Python. Ideally we would like you to install the latest version of Python, however if you already have an earlier version installed that should work too! At a minimum, this tutorial requires Python 3.5.


{{% notice info %}}  
This section is based on [a tutorial by Geek Girls Carrots](https://github.com/ggcarrots/django-carrots).
{{% /notice %}}


## Check your version of Python

We're going to perform a simple experiment to check whether Python is already installed, and if it is, what version is installed.

Open the *Terminal* application of your choice (if you don't know what the terminal is feel free to ask a mentor) and enter the following command, depending on your operating system:

### Mac/Linux Users:
```shell
python3 --version
```

### Windows Users
```shell
py --version
```

If the command returns `Python 3.Y.Z` congratulations you have Python installed! Otherwise you will have to install Python on your machine. How to do this will vary depending on your system, see below for instructions on how to do this for some common systems.


### GitHub Codespaces

If your local environment is restrictive, you can run the lab using GitHub Codespaces. It allows you to write code in the browser remotely! All you need is a GitHub account, then you can run the Codespaces from your browser.

If you would like to give GitHub Codespaces a try, you can skill this section, and connect to VS Code using codespaces in the next section.


## Install on Windows

First check whether your computer is running a 32-bit version or a 64-bit version of Windows, by pressing the Windows key + Pause/Break key which will open your System info, and look at the "System type" line. You can download Python for Windows from the website https://www.python.org/downloads/windows/. Click on the "Latest Python 3 Release - Python x.x.x" link. If your computer is running a **64-bit** version of Windows, download the **Windows x86-64 executable installer**. Otherwise, download the **Windows x86 executable installer**. After downloading the installer, you should run it (double-click on it) and follow the instructions there.

One thing to watch out for: During the installation you will notice a window marked "Setup". Make sure you tick the "Add Python 3.x to PATH" checkbox and click on "Install Now", as shown below.

- If you forget to tick above checkbox, the easiest way is to uninstall and re-install with the option ticked.
- If `Microsoft Store` opens up when you run 'python' command in terminal, you can install python from the store directly. It will configure python environment for you.

![Don't forget to add Python to the Path](images/python-installation-options.png)

In upcoming steps, you'll be using the Windows Command Line (which we'll also tell you about). For now, if you need to type in some commands, go to Start menu → All Programs → Accessories → Command Prompt. You can also hold in the Windows key and press the "R"-key until the "Run" window pops up. To open the Command Line, type "cmd" and press enter in the "Run" window. (On newer versions of Windows, you might have to search for "Command Prompt" since it's sometimes hidden.)

![Type "cmd" in the "Run" window](images/windows-plus-r.png)

{{% notice tip %}}
If you are using an older version of Windows (7, Vista, or any older version) and the Python installer fails with an error, you can try either:  
Install all Windows Updates and try to install Python again  
**Or**  
Install an [older version of Python](https://www.python.org/downloads/windows/), e.g., [3.4.4](https://www.python.org/downloads/release/python-344/).
{{% /notice %}}

If you install an older version of Python, the installation screen may look a bit different than shown above. Make sure you scroll down to see "Add python.exe to Path", then click the button on the left and pick "Will be installed on local hard drive":

![Add Python to the Path, older versions](images/add_python_to_windows_path.png)

## Install on Mac

{{% notice note %}}
Before you install Python on OS X, you should ensure your Mac settings allow
 installing packages that aren't from the App Store.  
 Go to System Preferences (it's in the Applications folder), click
 "Security & Privacy," and then the "General" tab.  
 If your "Allow apps downloaded from:" is set to "Mac App Store," change it
 to "Mac App Store and identified developers."
{{% /notice %}}

You need to go to the website https://www.python.org/downloads/ and download the latest version of the Python installer:

* Download the *Mac OS X 64-bit/32-bit installer* file,
* Double click *python-3.x.x-macosx10.x.pkg* to run the installer.

## Install on Linux

It is very likely that you already have Python installed out of the box. To check if you have it installed (and which version it is), open a console and type the following command:

<!-- {% filename %}command-line{% endfilename %} -->
```
$ python3 --version
Python 3.7.3
```

If you have a different 'micro version' of Python installed, e.g. 3.7.0, then you don't have to upgrade. If you don't have Python installed, or if you want a different version, you can install it as follows:

## Install for Debian and Ubuntu

Type this command into your console:

<!-- {% filename %}command-line {% filename %} -->
```
$ sudo apt-get install python3
```

## Fedora (up to 21)

Use this command in your console:

<!-- {% filename %}command-line<!-- {% filename %} -->
```
$ sudo yum install python3
```

## Fedora (22+)

Use this command in your console:

<!-- {% filename %}command-line<!-- {% filename %} -->
```
$ sudo dnf install python3
```

## openSUSE

Use this command in your console:

<!-- {% filename %}command-line<!-- {% filename %} -->
```
$ sudo zypper install python3
```

Verify the installation was successful by opening the *Terminal* application and running the `python3` command:

<!-- {% filename %}command-line<!-- {% filename %} -->
```
$ python3 --version
Python 3.7.3
```

{{% notice note %}}
If you're on Windows and you get an error message that `python3` wasn't found, try using `python` (without the `3`) and check if it still might be a version of Python 3.
{{% /notice %}}

----

If you have any doubts, or if something went wrong and you have no idea what to do next, please ask a mentor!
