import urllib2

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

book = urllib2.urlopen('https://www.gutenberg.org/ebooks/1342.txt.utf-8')

book_text = book.read().decode('utf-8')

tokens = word_tokenize(book_text)
text = nltk.Text(tokens)

# print book_text
# print book_text[0:20]
# print tokens[0:10]
# print text.collocations()
print text.concordance('lizzy')
# print text.similar('park')

