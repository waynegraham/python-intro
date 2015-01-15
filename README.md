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

### Something "Useful"

Doing computational work requires data. One useful definition of data from the Univeristy of Minnesota is "[a] reinterpretable representation of information in a formalized manner suitable for communication, interpretation, or processing." While there are different types of data, the data that we can use for computational work is digital data.

For this workshop, we will use data from the Digital Public Library of America, which is working to aggregate and make available data from cultural heritage institutions across the United States. We can take this data and use it to find items of interest and trends across the contributing organizations.

To do that, we first need to get a key from the DPLA so that we can gain access to the data. We will then interact with the API through our browsers and examine just what this data looks like to think about the types of questions we can explore using it.

#### 1. Get an API Key
Go to [http://dp.la/info/developers/codex/](http://dp.la/info/developers/codex/). This is the documentation for the DPLA API. Remember from our earlier conversation that an API is an interface that allows computer programs to talk to one another: if you format your request in a particular way, you will get back the data from the server in a particular data format without any surrounding HTML.

First, you will need an API key.

If you are on a Mac, there is a utility built into your system called "cURL". To use cURL to request your key, type:

```
$ curl -v -XPOST http://api.dp.la/v2/api_key/YOUR_EMAIL@example.com
```

into your Terminal, replacing "YOUR_EMAIL@example.com" with your actual email address.

If you are on Windows, your utility is called "Invoke-WebRequest". To use Invoke-WebRequest to request your key, type:

```
Invoke-WebRequest -Uri ("http://api.dp.la/v2/api_key/YOUR_EMAIL@example.com") -Method POST -Verbose
```

into Powershell, replacing "YOUR_EMAIL@example.com" with your actual email address.

You should get an email from the DPLA with your key.

#### 2.  Examining Data in a Browser

To get a sense of how the API key works and what the data we get back looks like, let's use the web-browser. If you can, please use [Chrome](https://www.google.com/chrome/).

In your browser, type:

```
http://api.dp.la/v2/items?q=cooking&api_key=YOURAPIKEY
```

replacing "YOURAPIKEY" with the key just emailed to you.

The first part of this URL ("http://api.dp.la/v2/") is the "base" URL. This must go at the beginning of all API requests. Next, we are telling the server that we want to see "items" and we want to see the items that match the keyword "cooking". The "`?q=`" is the grammar of the API – this is how we signal to the server that we want to query for the word following the "`=`". To see additional options for the API, go to [http://dp.la/info/developers/codex/requests/](http://dp.la/info/developers/codex/requests/).

You should see something that looks like:

```json
{"count":10646,"start":0,"limit":10,"docs":[{"@context":"http://dp.la/api/items/context","isShownAt":"https://digital.lib.ecu.edu/7394","dataProvider":"East Carolina University","@type":"ore:Aggregation","provider":{"@id":"http://dp.la/api/contributor/digitalnc","name":"North Carolina Digital Heritage Center"},"object":"https://digital.lib.ecu.edu/encore/ncgre000/00000008/00007394/00007394_tn_0001.gif","ingestionSequence":14,"id":"7cb32765b538a57a35fbdbfad03be57b","ingestDate":"2014-08-19T10:45:46.393447","_rev":"2-1b21f198053a2727bffece028cd30a6d","aggregatedCHO":"#sourceResource","_id":"digitalnc--urn:brevard.lib.unc.eduecu_c5:oai:digital.lib.ecu.edu/7394"
```
Well done! You have just made a successful API request.

#### 3. Thinking about JSON
What you are looking at is a JSON document. In JSON, all the information is given in "key : value" pairs. On the left-hand side is the "key". This is a standardized description of bits of information, such as "provider" or "ingestData". On the right-hand side is the "value", or the information that applies for a particular item. With your table, look at the JSON document in your browser and try to answer the following questions:

1. Look at the search results: how many objects are displayed here? How do you know?
1. How many objects in the DPLA database fit the query for *cooking*?
2. What questions might you ask of this dataset? Which key:value pairs would be most helpful for answering those questions?
3. What questions would be hard to answer with this dataset? What additional information would you need?

#### 4. Install DPyLA Library
The DPyLA library makes it easy to work with the DPLA API than manually writing everything yourself. In your terminal, use `pip` to install `dpla`.

```
$ pip install dpla
```

If you run in to permission issues, you may need to type `sudo` at the beginning of the line. What does `sudo` do?

#### 5. A Program with DPLA

Open a new file (e.g. `dpla-example.py`) in your text editor, and let's set up a program to interact with DPLA:

```python
from dpla.api import DPLA  

dpla = DPLA('your-key-here')
result = dpla.search('cooking')

print result.items[0:3]

```

What does the line `print result.items[0:3]` mean?

#### 6. NLTK

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

Get a dummy dataset by downloading a prepared dataset:

```
$ curl -O https://raw.githubusercontent.com/waynegraham/python-intro/master/text_results.txt .
```

Create a new file `text_mining.py` and add the following:

```python
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

with open('text_results.txt', 'r') as file:
    cooking_text = file.read().decode('utf8')

# Define Functions
cooking_tokens = word_tokenize(cooking_text)
text = nltk.Text(cooking_tokens)

# Make Function Calls
#print cooking_text[0:20]
#print cooking_tokens[0:10]
#print text.collocations()
#print text.concordance('lip')
print text.similar('Pot')

```

What happens when you run this? What happens when you remove the '#' from the different print lines?

#### 6. Share Your Code

Add the files you created to `git`, create a [good message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) about them, and push it to Github. 


## Reflection

Git is one of the most powerful, useful tools you will be introduced to this semester. Github will allow you to share the work you're creating with your collegues, and with wider audiences. This can be part of your professional credentials and contributes to building your online identity. No matter what people tell you, writing software is an inheritenly social endeavor, it's a way of communicating your intent to other developers in a way that can be executed by computers. 

## Resources

* [Make Your Code Citable](https://guides.github.com/activities/citable-code/)
* [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [Getting Your Project on Github](https://guides.github.com/introduction/getting-your-project-on-github/)






