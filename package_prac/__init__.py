from package_prac import utils

__version__ = '0.10.3'

def get_wordcounts(x):
	'''Providing no of words in a paragraph'''
	return utils.get_wordcounts1(x)

def get_charcounts(x):
	'''Providing no of characters'''
	return utils.get_charcounts1(x)

def get_avg_wordlength(x):
	'''Provinding the avg word length of that paragraph'''
	return utils.get_avg_wordlength1(x)

def get_stopwords_counts(x):
	'''Providing no of stop words present'''
	return utils.get_stopwords_counts1(x)

def get_hashtag_counts(x):
	'''Providing no of hashtag present'''
	return utils.get_hashtag_counts1(x)

def get_mentions_counts(x):
	'''Providing no of mentions in a paragraph '''
	return utils.get_mentions_counts1(x)

def get_digit_counts(x):
	'''Providing no of digits in a paragraph'''
	return utils.get_digit_counts1(x)

def get_uppercase_counts(x):
	'''Providing of number of uppercase letters'''
	return utils.get_uppercase_counts1(x)

def cont_exp(x):
	'''Couting expressions in a paragraph'''
	return utils.cont_exp1(x)

def get_emails(x):
	'''Countng no of emails present '''
	return utils.get_emails1(x)

def remove_emails(x):
	'''Removing emails from a paragraph'''
	return utils.remove_emails1(x)

def get_urls():
	'''Getting all urls from a paragraph'''
	return utils.get_urls1(x)

def remove_urls(x):
	'''Removing all the urls'''
	return utils.remove_urls1(x)

def remove_rt(x):
	return utils.remove_rt1(x)

def remove_special_chars(x):
	'''Removing all the special characters'''
	return utils.remove_special_chars1(x)

def remove_html_tags(x):
	'''Removing all the html tags'''
	return utils.remove_html_tags1(x)

def remove_accented_chars(x):
	'''Removing all the accented characters'''
	return utils.remove_accented_chars1(x)

def remove_stopwords(x):
	''' Removing all the stopwords'''
	return utils.remove_stopwords1(x)

def make_base(x):
	'''Converting all words to base form'''
	return utils.make_base1(x)

def get_value_counts(df, col):
	'''Returning value counts of paragraph'''
	return utils.get_value_counts1(df, col)

def get_word_freqs(df, col):
	'''Calculating words frequencies'''
	return utils.get_value_counts1(df, col)

def remove_common_words(x, freq, n=20):
	'''Removing all the common words'''
	return utils.remove_common_words1(x, freq, n)

def remove_rarewords(x, freq, n=20):
	'''Removing all the rare words'''
	return utils.remove_rarewords1(x, freq, n)

def spelling_correction(x):
	'''Correct all the spellings in a paragraph'''
	return utils.spelling_correction1(x)

def remove_dups_char(x):
	'''Removing all the duplicate characters'''
	return utils.remove_dups_char1(x)

def get_basic_features(df):
	return utils.get_basic_features1(df)

def get_ngram(df, col, ngram_range):
	return utils.get_ngram1(df, col, ngram_range)