---
title: "2. Installation"
weight: 2
chapter: true
---

# Installation

In this section you will be building a Bakery app. As you go through the tutorial, you'll be instructed on how to install various software on your computer and set up some online accounts as needed.

---

## MacOS, Windows, Linux Installation

### Brief intro to the command line

Many of the steps below reference the "console", "terminal", "command window", or "command line" -- these all mean the same thing.

#### Opening the command line

- **macOS:** Go to **Launchpad → Other → Terminal**.
- **Linux:** Usually found under **Applications → Accessories → Terminal**.
- **Windows:** 
  - Search **Command Prompt** in the Start menu.
  - Open **Windows System → Command Prompt**.
  - Use `Win + R`, type `cmd`, and press Enter.

#### Install Python

Django is written in Python, so we need Python installed:

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

If not, install it based on your Linux distribution:

```sh
sudo apt install python3   # Debian/Ubuntu
sudo dnf install python3   # Fedora
sudo zypper install python3  # openSUSE
```

### Install a Code Editor

We recommend installing a text editor for coding:

- **[Visual Studio Code](https://code.visualstudio.com/)** (recommended)

### Set up virtual environment and install Django

#### Create a virtual environment

In your home directory, create a new project folder:

```sh
mkdir djangogirls
cd djangogirls
```

Create a virtual environment:

```sh
python3 -m venv myvenv
```

#### Activate the virtual environment

**Windows:**

```sh
myvenv\Scripts\activate
```

**Linux/macOS:**

```sh
source myvenv/bin/activate
```

#### Install Django

1. Ensure you have the latest **pip**:

```sh
pip install --upgrade pip
```

2. Create a `requirements.txt` file and add:

```
Django~=5.1.2
```

3. Install dependencies:

```sh
pip install -r requirements.txt
```

---

### Chromebook Installation

To set up your Chromebook, follow the instructions below:

1. **Go to GitHub.com** and sign up for a new, free user account.
2. **Create a GitHub project.** Visit this link, use `Bakery_app` name for your project, and make it public.
3. **Start a Codespace.** Go to GitHub Codespaces and select the repository you just created. Click **Create Codespace**.
4. **Wait for the VSCode editor to open automatically.** If prompted, install Python from the Extensions tab.
5. **Continue with the tutorial.** Follow the next steps from the section **Set up virtual environment and install Django**. Follow the Ubuntu/Linux sections using the Codespaces command line (terminal).
