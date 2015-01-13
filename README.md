# Intro to Git and Python

* Text Editor ([Atom](https://atom.io) or [SublimeText](http://www.sublimetext.com))
* [Git](http://git-scm.com/download/)
* Python ([latest 2.7 release](https://www.python.org/downloads/))
* Account on [Github](https://github.com)
* Github client (https://windows.github.com/ or https://mac.github.com/)

## Shell

This is an alternative method of working with your computer. Commands
you need to know:

```
cd    # change directory (move to a new directory)
ls    # list files in a directory
pwd   # present working directory
touch # create an empty file
rm    # remove file
mkdir # make directory
cp    # copy file
mv    # move file
man   # documentation for command
```

  > *Tips*: up arrow repeats previous command; tab auto-completes file
  > names

## Git

!['final'.doc](http://www.phdcomics.com/comics/archive/phd101212s.gif)

[Try Git](https://try.github.io)

## Github
Nothing directly to do with `git`.

## Workshop

Create a new `git` repository, write a short Python program, and share it on Github.

Open the bash prompt that was included in Git (for OS X users, open the `Terminal` app). Create a new project directy and change in to it:

```
$ mkdir -p projects/workshop
$ cd projects/workshop
```

Intialize a new `git` repository:

```
$ git init
```

Create a new file and open it in your text editor:

```
$ touch example.py
$ atom example.py
```

(Windows PowerShell users may need)

```
$ New-Item -ItemType file example.py
$ Start atom example.py
```

In the editor type `print "Hello World"`

Save your program, and in the console/terminal, type:

```
$ python example.py
```

You should see the text "`Hello World`" printed on the terminal.

### Create a Repository

A **repository** is the basic unit of GitHub, most commonly a single project. Repositories can contain folders and files, including images - anything your project needs. Because we recommend including a README, or a file describing the project, in every repository, GitHub makes it easy to add one at the same time you create your new repository. *It also offers other common options such as a license file, but we can skip that for now.*

#### To create a new repository

1. Click the  icon next to your username, top-right.
2. Name your repository hello-world.
3. Write a short description.
4. Select Initialize this repository with a README.

![New Repository](https://guides.github.com/activities/hello-world/create-new-repo.png)

Click **Create repository**. Boom, repository! :boom:

#### Make a commit

In `git`, saved chages are called **commits**. Commits are pretty glorious, because a bunch of them together read like the history of your project.

Each commit has an associated **commit message**, which is a description explaining why a particular change was made. Thanks to these messages, you and others can read through commits and understand what you’ve done and why.

(adapted from https://guides.github.com/activities/hello-world/)

## Resources

* [Make Your Code Citable](https://guides.github.com/activities/citable-code/)
* [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [Getting Your Project on Github](https://guides.github.com/introduction/getting-your-project-on-github/)






