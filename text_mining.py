#! /usr/bin/env python

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
#print text.similar('Pot')
