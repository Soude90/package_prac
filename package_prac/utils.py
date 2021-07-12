import re
import os
import sys
import json

import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob
import en_core_web_sm

from sklearn.feature_extraction.text import CountVectorizer

nlp = en_core_web_sm.load()

path = os.path.dirname(os.path.abspath(__file__))
abbreviations_path = os.path.join(path, 'data','abbreviations_wordlist.json')


def get_wordcounts1(x):
	length = len(str(x).split())
	return length

def get_charcounts1(x):
	s = x.split()
	x = ''.join(s)
	return len(x)

def get_avg_wordlength1(x):
	count = get_charcounts1(x)/get_wordcounts1(x)
	return count

def get_stopwords_counts1(x):
	l = len([t for t in x.split() if t in stopwords])
	return l

def get_hashtag_counts1(x):
	l = len([t for t in x.split() if t.startswith('#')])
	return l

def get_mentions_counts1(x):
	l = len([t for t in x.split() if t.startswith('@')])
	return l

def get_digit_counts1(x):
	digits = re.findall(r'[0-9,.]+', x)
	return len(digits)

def get_uppercase_counts1(x):
	return len([t for t in x.split() if t.isupper()])

def cont_exp1(x):
	abbreviations = json.load(open(abbreviations_path))

	if type(x) is str:
		for key in abbreviations:
			value = abbreviations[key]
			raw_text = r'\b' + key + r'\b'
			x = re.sub(raw_text, value, x)
			# print(raw_text,value, x)
		return x
	else:
		return x


def get_emails1(x):
	emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', x)
	counts = len(emails)

	return counts, emails


def remove_emails1(x):
	return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)

def get_urls1(x):
	urls = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)
	counts = len(urls)

	return counts, urls

def remove_urls1(x):
	return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)

def remove_rt1(x):
	return re.sub(r'\brt\b', '', x).strip()

def remove_special_chars1(x):
	x = re.sub(r'[^\w ]+', "", x)
	x = ' '.join(x.split())
	return x

def remove_html_tags1(x):
	return BeautifulSoup(x, 'lxml').get_text().strip()

def remove_accented_chars1(x):
	x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
	return x

def remove_stopwords1(x):
	return ' '.join([t for t in x.split() if t not in stopwords])	

def make_base1(x):
	x = str(x)
	x_list = []
	doc = nlp(x)
	
	for token in doc:
		lemma = token.lemma_
		if lemma == '-PRON-' or lemma == 'be':
			lemma = token.text

		x_list.append(lemma)
	return ' '.join(x_list)

def get_value_counts1(df, col):
	text = ' '.join(df[col])
	text = text.split()
	freq = pd.Series(text).value_counts()
	return freq

def remove_common_words1(x, freq, n=20):
	fn = freq[:n]
	x = ' '.join([t for t in x.split() if t not in fn])
	return x

def remove_rarewords1(x, freq, n=20):
	fn = freq.tail(n)
	x = ' '.join([t for t in x.split() if t not in fn])
	return x

def remove_dups_char1(x):
	x = re.sub("(.)\\1{2,}", "\\1", x)
	return x

def spelling_correction1(x):
	x = TextBlob(x).correct()
	return x

def get_basic_features1(df):
	if type(df) == pd.core.frame.DataFrame:
		df['char_counts'] = df['text'].apply(lambda x: _get_charcounts(x))
		df['word_counts'] = df['text'].apply(lambda x: _get_wordcounts(x))
		df['avg_wordlength'] = df['text'].apply(lambda x: _get_avg_wordlength(x))
		df['stopwords_counts'] = df['text'].apply(lambda x: _get_stopwords_counts(x))
		df['hashtag_counts'] = df['text'].apply(lambda x: _get_hashtag_counts(x))
		df['mentions_counts'] = df['text'].apply(lambda x: _get_mentions_counts(x))
		df['digits_counts'] = df['text'].apply(lambda x: _get_digit_counts(x))
		df['uppercase_counts'] = df['text'].apply(lambda x: _get_uppercase_counts(x))
	else:
		print('ERROR: This function takes only Pandas DataFrame')
		
	return df


def get_ngram1(df, col, ngram_range):
	vectorizer = CountVectorizer(ngram_range=(ngram_range, ngram_range))
	vectorizer.fit_transform(df[col])
	ngram = vectorizer.vocabulary_
	ngram = sorted(ngram.items(), key = lambda x: x[1], reverse=True)

	return ngram
