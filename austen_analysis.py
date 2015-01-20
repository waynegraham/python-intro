import urllib2

book = urllib2.urlopen('https://www.gutenberg.org/ebooks/1342.txt.utf-8')

book_text = book.read().decode('utf-8')

print book_text

