from package_prac import utils

__version__ = '0.10.3'

def get_wordcounts(x):
	return utils.get_wordcounts1(x)

def get_charcounts(x):
	return utils.get_charcounts1(x)

def get_avg_wordlength(x):
	return utils.get_avg_wordlength1(x)

def get_stopwords_counts(x):
	return utils.get_stopwords_counts1(x)

def get_hashtag_counts(x):
	return utils.get_hashtag_counts1(x)

def get_mentions_counts(x):
	return utils.get_mentions_counts1(x)

def get_digit_counts(x):
	return utils.get_digit_counts1(x)

def get_uppercase_counts(x):
	return utils.get_uppercase_counts1(x)

def cont_exp(x):
	return utils.cont_exp1(x)

def get_emails(x):
	return utils.get_emails1(x)

def remove_emails(x):
	return utils.remove_emails1(x)

def get_urls():
	return utils.get_urls1(x)

def remove_urls(x):
	return utils.remove_urls1(x)

def remove_rt(x):
	return utils.remove_rt1(x)

def remove_special_chars(x):
	return utils.remove_special_chars1(x)

def remove_html_tags(x):
	return utils.remove_html_tags1(x)

def remove_accented_chars(x):
	return utils.remove_accented_chars1(x)

def remove_stopwords(x):
	return utils.remove_stopwords1(x)

def make_base(x):
	return utils.make_base1(x)

def get_value_counts(df, col):
	return utils.get_value_counts1(df, col)

def get_word_freqs(df, col):
	return utils.get_value_counts1(df, col)

def remove_common_words(x, freq, n=20):
	return utils.remove_common_words1(x, freq, n)

def remove_rarewords(x, freq, n=20):
	return utils.remove_rarewords1(x, freq, n)

def spelling_correction(x):
	return utils.spelling_correction1(x)

def remove_dups_char(x):
	return utils.remove_dups_char1(x)

def get_basic_features(df):
	return utils.get_basic_features1(df)

def get_ngram(df, col, ngram_range):
	return utils.get_ngram1(df, col, ngram_range)