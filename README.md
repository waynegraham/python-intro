# Intro to Git and Github with Python

This is what you need to ensure everything will work properly for this
session.

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

[Try Git](https://try.github.io)

['final'.doc](http://www.phdcomics.com/comics/archive/phd101212s.gif)


## Github
Github is a social code sharing site; it is something completely
different than the command-line `git` tool.

## Practice

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
$ subl example.py
```

  > OS X users can create a terminal link to Sublime Text with `ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" ~/bin/subl`
  > **Windows** users can do this, but it's a bit more involved. See this
  > [Stack Overflow post](http://stackoverflow.com/questions/9440639/sublime-text-from-command-line-win7)

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

#### Push to GitHub

In `git`, you have to **push** your changes to a remote place before it
shows up. In the GitHub client, this is renamed "Sync" and allows you to
get the lastest changes everywhere they need to be.

1. Click on the name of the repository you're working with.
2. You'll see a view that lists all of your recent changes. Add a commit message and description to commit your changes
3. When you're ready to share your changes, click the blue **Sync**
   button in the upper-right corner.

![commit](https://help.github.com/assets/images/windows/commits/windows_commit.png)


(adapted from https://guides.github.com/activities/hello-world/)

### Something "Useful"

Doing computational work requires data. One useful definition of data from the Univeristy of Minnesota is "[a] reinterpretable representation of information in a formalized manner suitable for communication, interpretation, or processing." While there are different types of data, the data that we can use for computational work is digital data.

For this workshop, we will use data from Project Gutenberg (*Pride and
Prejudice*) that we will programmatically download and analyze.

#### 1. Downloading a Book

From the [top 100](https://www.gutenberg.org/browse/scores/top) list of
books on the site, I took the top-downloaded book. If you navigate your
browser to the project page for [Pride and Prejudice](https://www.gutenberg.org/ebooks/1342), you will see a list of download formats. For this exercise, we need the '[**Plain Text UTF-8**](https://www.gutenberg.org/ebooks/1342.txt.utf-8)' version.

In a new file in your project directory, create `austen_analysis.py`. In
it, we need to import the Python library we need to download web content
(`urllib2`) and set up the download mechanism.

```python
import urllib2

book = urllib2.urlopen('https://www.gutenberg.org/ebooks/1342.txt.utf-8')

book_text = book.read().decode('utf-8')

print book_text
```

Don't get too hung up on the syntax, but basically this opens a web
connection to the url (https://www.gutenberg.org/ebooks/1342.txt.utf-8),
then reads the content and ensures that the content is decoded using UTF-8 standards.

In your terminal, run the script (`python austen_analysis.py`). If
everything goes well, you should see the terminal print *Pride and
Prejudice* to the screen.

```
...
This Web site includes information about Project Gutenberg-tm,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.
```

#### 2. Git Cycle

Now that something is working, it's time to let `git` know about it.
From the terminal, run `git status` to see what `git` knows about.

```
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	austen_analysis.py
```

Now we need to tell `git` to track changes in the `austen_analysis.py`
file.

  $ git add austen_analysis.py

Run `git status` again and you will see that it has moved in the output:

```
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   austen_analysis.py
```

Now we commit (with a good commit message):

  git commit -m "Download PaP from Proj. Gutenberg"

  > If you forget to '-m' and ever get stuck, type "**:x**" to get out
  > of vim.

The last step is to push this change to GitHub to "publish" the code.

  git push origin master

This last step isn't necessary for every commit, just when you are ready
to share the code.

#### 2. NLTK

Ensure you have the `stopwords` and tokenizer lists installed. In your Python interpretor, import nltk and download stopwords tokenizer (punkt).

```shell
Python 2.7.9 (default, Dec 10 2014, 23:46:04)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import nltk
>>> nltk.download('stopwords')
>>> nltk.download('punkt')
>>> quit()
```

In your editor (with `austen_analysis.py` open), we need to import a few
more libraries to do some analysis, stopwords and a word tokenizer.

```python
import urllib2

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

book = urllib2.urlopen('https://www.gutenberg.org/ebooks/1342.txt.utf-8')

book_text = book.read().decode('utf-8')

print book_text

```

Now comment out `print book_text`. Under that line, add the following to
calculate the tokens and prepare the book for analysis:

```python
tokens = word_tokenize(book_text)
text = nltk.Text(tokens)
```

Now that we have that in place, we can print various components of the
text by adding the following:

```python
#print book_text[0:20]
#print tokens[0:10]
#print text.collocations()
print text.concordance('lizzy')
#print text.similar('park')
```

What happens when you run this? What happens when you remove the '#' from the different print lines?

If you've gotten turned around somewhere, this is the full script:

```python
import urllib2
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize


book = urllib2.urlopen('https://www.gutenberg.org/ebooks/1342.txt.utf-8')
book_text = book.read().decode('utf-8')

tokens = word_tokenize(book_text)
text = nltk.Text(tokens)

#print book_text[0:20]
#print tokens[0:10]
#print text.collocations()
print text.concordance('lizzy')
#print text.similar('park')
```

What are the steps at this point?

* `git status`
* `git add`
* `git commit`
* `git push`

#### 6. Share Your Code

Add the files you created to `git`, create a [good message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) about them, and push it to Github. 


## Reflection

Git is one of the most powerful, useful tools you will be introduced to this semester. Github allows you to share the work you're creating with your collegues, and with wider audiences. This can be part of your professional credentials and contributes to building your online identity. No matter what people tell you, writing software is an inheritenly social endeavor, it's a way of communicating your intent to other developers in a way that can be executed by computers. 

## Resources

* [Make Your Code Citable](https://guides.github.com/activities/citable-code/)
* [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [Getting Your Project on Github](https://guides.github.com/introduction/getting-your-project-on-github/)






