<p align="center">
  <br>
  <img width="200" src="./splash.jpg">
  <br>
  <br>
</p>

## Social Networks PMS


> Repo containing resources for the Social Networks Analysis course (PMS @ AUTh CS Dept.)

Instructors: Ilias Dimitriadis (idimitriad@csd.auth.gr), Vasilis Souvatzis (vasisouv@csd.auth.gr)

- [Python Installation](#python-installation)
    - [Windows](#windows)
    - [Linux](#linux)
    - [Mac](#mac)
- [Setting up a virtual environment](#setting-up-a-virtual-environment)
    - [Installing required packages from requirements.txt](#environment-requirements)
    

# Python Installation

We are going to be using python 3.6 for these lessons (despite 3.7 being the latest stable release) to avoid possible packages incompatibilities.

### Windows

1. Download the [official Python installer (v3.6.5)](https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe)
2. Run the executable and proceed with the installation. (IMPORTANT: You want to be sure to check the box that says Add Python 3.x to PATH as shown below to ensure that the interpreter will be placed in your execution path.)

<p align="center">
  <br>
  <img width="300" src="./win-python-install.png">
  <br>
  <br>
</p>

### Linux

- Ubuntu:

`$ sudo apt-get update`

`$ sudo apt-get install python3.6`

NOTE: If you are using Ubuntu 14.04 or 16.04, Python 3.6 is not in the Universe repository, and you need to get it from a Personal Package Archive (PPA). For example, to install Python from the “deadsnakes” PPA, do the following:

`$ sudo add-apt-repository ppa:deadsnakes/ppa`

`$ sudo apt-get update`

`$ sudo apt-get install python3.6`

- Arch

` packman -S python `

For other versions check [this link](https://realpython.com/installing-python/)


### Mac

A detailed step-by-step guide can be found [here](https://realpython.com/installing-python/#macos-mac-os-x)

# Setting up a virtual environment 

Virtual environments are isolated python interpreters for each project or a group of projects. Creatinng  a virtual environment for every new python project allows you to have different versions of each module installed in every isolated environment, ensuring less module conflicts.

Some editors/IDEs like [Jetbrain's PyCharm](https://www.jetbrains.com/pycharm/download/), [Sublime Text](https://www.sublimetext.com/3), [Visual Studio Code](https://code.visualstudio.com/Download) or [Atom](https://atom.io/) have graphical interfaces for creating such environments. If you use some of the above check out the corresponding links:

- [PyCharm venv](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
- [Sublime venv](https://packagecontrol.io/packages/Virtualenv)
- [Visual Studio Code venv](https://code.visualstudio.com/docs/python/environments)
- [Atom venv](https://atom.io/packages/atom-python-virtualenv)

If these links do not suite your needs, the command line approach is as follows:

1. Create a folder that will serve as your new project's root directory.
2. Open the terminal and navigate to that folder.
3. `pip install virtualenv`
4. `virtualenv  venv`
5. `source venv/bin/activate`

For any question or obstacle you may encounter, do not hesitate to contact us.