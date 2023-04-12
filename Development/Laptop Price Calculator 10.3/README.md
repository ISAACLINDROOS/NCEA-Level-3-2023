```diff
+ LATEST RELEASE
```
<p align="center" width="100%">
    <img width="33%" src="https://user-images.githubusercontent.com/21046313/180737799-9701e599-1668-4adc-bbe9-e7ced4d796b9.png">
</p>

# Isaac Lindroos: AS91896
### Use advanced programming techniques to develop a computer program (Level 2, 6 credits)

#### Task:
Create a program that works as a tool to allow users to solve a specific problem.  

#### Problem: 
Parents and students would like a Budget Laptop Calculator to assist them in figuring out the prices of a laptop that is fit for purpose at school. For example, the student needs his laptop for 3d modelling, must have a minimum RAM of 16GB, this tool would suggest possible laptops and a predicted budget.

You need to think about the context this calculator would be used in, the end users and the usability of such a tool and plan accordingly. You are encouraged to refine and redesign your calculator interface based on your own goals.  

#### Your task is to create a functional prototype to suit the needs of your potential users. You may create a text-based program or a GUI interface (which will require a library like tkinter or PyQt5).
- - - -
# Prerequisites
To successfully run this program, you need to first setup your Python development environment. Specifically, this program requires:

## Software & Extensions:
* VS Code
* The VS Code Python extension
* Python 3 or later

## Environments:

* `pip`	

The Python package manager that installs and updates packages. It's installed with Python 3.9+ by default (install python3-pip on Debian-based OSs).

* `venv`

Allows you to manage separate package installations for different projects and is installed with Python 3 by default (install python3-venv if you are using a Debian-based OS)

* `conda`	

Installed with Anaconda and Miniconda. It can be used to manage both packages and virtual environments. Generally used for data science projects.


### Create a virtual environment

To create a virtual environment, use the following command, where ".venv" is the name of the environment folder:

```shell
# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv

```
>Note: To learn more about the `venv` module, see Creation of virtual environments at https://docs.python.org/3/tutorial/venv.html

When you create a new virtual environment, a prompt will be displayed to allow you to select it for the workspace.

This will add the path to the Python interpreter from the new virtual environment to your workspace settings. That environment will then be used when installing packages and running code through the Python extension.

## Modules & Packages:

* Tkinter
* Tkinter Designer
* git
* pandas
- - - -

### Installing Tkinter Designer

There are Three options when installing Tkinter Designer:

#### Install with `pip`

```
pip install tkdesigner
```

#### Install with `poetry`

```
poetry new <gui_project_name> && cd <gui_project_name>
poetry add tkdesigner
poetry install
```

#### To run Tkinter Designer from the source code, follow the instructions below:

* Download the source files for Tkinter Designer by downloading it manually or using GIT.

```
git clone https://github.com/ParthJadhav/Tkinter-Designer.git
```

* Change your working directory to Tkinter Designer:

```
cd tkinter-designer
```

* Install the necessary dependencies by running:

```
pip install -r requirements.txt
```

> In the event that pip doesn't work, also try the following commands:
> ```
> pip3 install -r requirements.txt
> ```
> ```
> python -m pip install -r requirements.txt
> ```
> ```
> python3 -m pip install -r requirements.txt
> ```
> If this still doesn't work, ensure that Python is added to the `PATH`.

#### This will install all requirements and Tkinter Designer. Before you use Tkinter Designer you need to create a Figma File.
- - - -
### Installing Git

The first step to learning Git is to get it installed! You have several options, depending on your computer's operating system.

Once you've got it installed, follow the instructions in **Getting Ready** at the bottom of this document.

#### Windows

##### GitHub Desktop

The easiest way to install Git on Windows is to install the latest version of [GitHub Desktop](https://desktop.github.com/). GitHub Desktop is a graphical Git client, but it also installs the underlying Git binary (and keeps it up to date).

Once you've installed GitHub Desktop, run the "Git Shell" program that comes with it. This is how you'll interact with Git via a command-line interface.

Jump down to **Getting Ready** and follow the rest of the instructions there!

##### Official Download

You can also [download Git from the official web site](https://git-scm.com/downloads). During installation, you'll be asked how to adjust your PATH. If you choose "Use Git from Git Bash only," you'll need to use the Git Bash program that ships with Git to interact with Git.

If you choose "Use Git from the Windows Command Prompt," then you can also use Git from the command prompt and from PowerShell. In this case, the choice of whether to use Git Bash or a built-in Windows shell is up to you.

Once it's finished installing, jump down to **Getting Ready** and follow the rest of the instructions there!

#### OS X

###### Homebrew

If you use [Homebrew](http://brew.sh/), you can install Git using the following command:

    brew install git

##### Official Download

You can also [download an installer for Git rom the official web site](https://git-scm.com/downloads).

Once you have Git installed, follow the instructions in **Getting Ready**, below.

#### Getting Ready - Git

Now that you've got Git installed, let's make sure you can access it, and that it's fully set up for you to use.

From your shell (Git Shell, Git Bash, or other terminal application of your choosing), type the following, replacing `YOUR NAME` with — you guessed it — your name.

    git config --global user.name "YOUR NAME"

You'll also want to set up your email address.

    git config --global user.email "YOUR EMAIL ADDRESS"

Assuming these commands run without errors, you're good to go! Otherwise, you may need to double-check your Git installation.
- - - -
### Installing Pandas
#### Installation:
If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

Install it using this command:

```
C:\Users\Your Name>pip install pandas
```
#### Import Pandas:
Once Pandas is installed, import it in your applications by adding the `import` keyword:

````
import pandas
````
Now Pandas is imported and ready to use.

#### Pandas as pd:
Pandas is usually imported under the `pd` alias.
Create an alias with the `as` keyword while importing:
````
import pandas as pd
````
Now the Pandas package can be referred to as `pd` instead of `pandas`.

### Checking Pandas Version
The version string is stored under `__version__` attribute.
````
import pandas as pd

print(pd.__version__)
````
- - - -

# UI Design

## Figma:

### Create a Figma Account
* In a web browser, navigate to figma.com and click 'Sign up'.
* Enter your information, then verify your email.
* Create a new Figma Design file.
* Get started making your GUI.

### Figma Design Formatting

The code generated by Tkinter Designer is based on the names of elements from your Figma design and, as such, you need to name your elements accordingly. In Figma, rename your elements by double-clicking them in the Layers panel.

#### Button:
Figma Element Name: `Button`
Tkinter Element Name: `Button`

#### Line:
Figma Element Name: `Line`
Tkinter Element Name: `Line`

#### Text:
Figma Element Name: `Text`
Tkinter Element Name: `"Name it anything"`

#### Rectangle: 
Figma Element Name: `Rectangle`
Tkinter Element Name: `Rectangle`

#### Text Area: 
Figma Element Name: `TextArea`
Tkinter Element Name: `Text Area`

#### Text Box: 
Figma Element Name: `TextBox`
Tkinter Element Name: `Entry`

#### Image: 
Figma Element Name: `Image`
Tkinter Element Name: `Canvas.Image()`

- - - -

### Element Guide

First, create a Frame that will serve as your Tkinter Window.

##### Adding Images:

* Images can be created using shapes and/or images.
* If you use multiple shapes/images, you must group them together by selecting them all and pressing <kbd>CTRL/⌘</kbd> + <kbd>G</kbd>
* After that name the element or group as `"Image"`.

##### Text (Normal Text):

* Use the <kbd>T</kbd> key to activate the text tool, then add text as desired.
* Text does not have to be renamed for use in Tkinter Designer.
* Explicitly press the <kbd>Return</kbd> Or <kbd>Enter</kbd> Key to move to the next line. 

##### Entry (Single-Line User Input):

* Activate the Rectangle tool with <kbd>R</kbd>.
* Adjust the Rectangle to your liking.
* Make sure the Rectangle is named "TextBox".

##### Text Area (Multi-Line User Input):

* Activate the Rectangle tool with <kbd>R</kbd>.
* Adjust the Rectangle to your liking.
* Make sure the Rectangle is named "TextArea".

##### Rectangle:

* Activate the Rectangle tool with <kbd>R</kbd>.
* Adjust the Rectangle to your liking.
* Make sure the Rectangle is named "Rectangle".

##### Normal Button:

* Add a rectangle to serve as a button in your GUI.
* Optional: Add text for the button.
* Select the button (Rectangle), and any optional text, then group them with <kbd>CTRL/⌘</kbd> + <kbd>G</kbd>.
* Name the group "Button".
- - - -
# How to use the Laptop Price Calculator

This laptop calculator is designed to help people through the sometimes complicated and overwhelming process of selecting a new laptop.

#### A few things to note:
* This application is a work in progress and is constantly being updated, The best way to stay up-to-date with the latest version is to check for the latest release in [Releases](https://github.com/ISAACLINDROOS/AS91896/tree/main/Releases).
* This application runs off the x64 processor (CPU) architecture. This means the app supports only Intel processors and needs Rosetta to work on a Mac with Apple silicon.


> #### On Mac computers with Apple silicon, About This Mac shows an item labelled Chip, followed by the name of the chip:
>
> ![image](https://user-images.githubusercontent.com/21046313/180735934-94ad964f-1fea-4bb5-aadb-c41873a9e7e1.png)

Install the App by saving the latest file in the [Releases](https://github.com/ISAACLINDROOS/AS91896/tree/main/Releases) directory or select from the [Releases Menu](https://github.com/ISAACLINDROOS/AS91896/releases). Once the file has been downloaded, run the .exe file (If done correctly, the main window should open).

> #### On Mac computers with Apple silicon, you may need to install Rosetta. A window like the one below may pop-up, simply click "Install" to continue.
>
>![image](https://user-images.githubusercontent.com/21046313/180735660-6721e16e-9004-4ac2-8679-12bb2e467474.png)

When the Main window opens, Simply go step by step through the process of selecting each option until complete. When ready, hit the "Generate" button (This will open a new window with your results). 

You can also download your results as a PDF Export by clicking the "Download" button on the results window.

If required, You can exit the application at any time by simply clicking the Red "Exit" button.
