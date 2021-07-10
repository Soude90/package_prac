import re 
import os 
import sys
import spacy
import unicodedata
from textblob import TextBlob
nlp = spacy.load('en_core_web_sm')

# Converting into unicode format
def _strip_accents(text):

	try:
		text = unicode(text, 'utf-8')
	except NameError: # unicode is a default on python 3 
		pass

	text = unicodedata.normalize('NFD', text)\
		   .encode('ascii', 'ignore')\
		   .decode("utf-8")
	return str(text)


# Correcting the spelling using textblob
def _spell_check(x):
	x=TextBlob(str(x)).correct()
	return ''.join(x)



# Removing all the spaces
def _remove_space(x):
	x=' '.join(x.split())
	return x

# Expanding the contracted words
def _contration_to_expansion(x):
	contractions = { 
	"ain't": "am not / are not / is not / has not / have not",
	"aren't": "are not / am not",
	"can't": "cannot",
	"can't've": "cannot have",
	"'cause": "because",
	"could've": "could have",
	"couldn't": "could not",
	"couldn't've": "could not have",
	"didn't": "did not",
	"doesn't": "does not",
	"don't": "do not",
	"hadn't": "had not",
	"hadn't've": "had not have",
	"hasn't": "has not",
	"haven't": "have not",
	"he'd": "he had / he would",
	"he'd've": "he would have",
	"he'll": "he shall / he will",
	"he'll've": "he shall have / he will have",
	"he's": "he has / he is",
	"how'd": "how did",
	"how'd'y": "how do you",
	"how'll": "how will",
	"how's": "how has / how is / how does",
	"I'd": "I had / I would",
	"I'd've": "I would have",
	"I'll": "I shall / I will",
	"I'll've": "I shall have / I will have",
	"I'm": "I am",
	"i'm": "i am",
	"I've": "I have",
	"isn't": "is not",
	"it'd": "it had / it would",
	"it'd've": "it would have",
	"it'll": "it shall / it will",
	"it'll've": "it shall have / it will have",
	"it's": "it is",
	"let's": "let us",
	"ma'am": "madam",
	"mayn't": "may not",
	"might've": "might have",
	"mightn't": "might not",
	"mightn't've": "might not have",
	"must've": "must have",
	"mustn't": "must not",
	"mustn't've": "must not have",
	"needn't": "need not",
	"needn't've": "need not have",
	"o'clock": "of the clock",
	"oughtn't": "ought not",
	"oughtn't've": "ought not have",
	"shan't": "shall not",
	"sha'n't": "shall not",
	"shan't've": "shall not have",
	"she'd": "she had / she would",
	"she'd've": "she would have",
	"she'll": "she shall / she will",
	"she'll've": "she shall have / she will have",
	"she's": "she has / she is",
	"should've": "should have",
	"shouldn't": "should not",
	"shouldn't've": "should not have",
	"so've": "so have",
	"so's": "so as / so is",
	"that'd": "that would / that had",
	"that'd've": "that would have",
	"that's": "that has / that is",
	"there'd": "there had / there would",
	"there'd've": "there would have",
	"there's": "there has / there is",
	"they'd": "they had / they would",
	"they'd've": "they would have",
	"they'll": "they shall / they will",
	"they'll've": "they shall have / they will have",
	"they're": "they are",
	"they've": "they have",
	"to've": "to have",
	"wasn't": "was not",
	"we'd": "we had / we would",
	"we'd've": "we would have",
	"we'll": "we will",
	"we'll've": "we will have",
	"we're": "we are",
	"we've": "we have",
	"weren't": "were not",
	"what'll": "what shall / what will",
	"what'll've": "what shall have / what will have",
	"what're": "what are",
	"what's": "what has / what is",
	"what've": "what have",
	"when's": "when has / when is",
	"when've": "when have",
	"where'd": "where did",
	"where's": "where has / where is",
	"where've": "where have",
	"who'll": "who shall / who will",
	"who'll've": "who shall have / who will have",
	"who's": "who has / who is",
	"who've": "who have",
	"why's": "why has / why is",
	"why've": "why have",
	"will've": "will have",
	"won't": "will not",
	"won't've": "will not have",
	"would've": "would have",
	"wouldn't": "would not",
	"wouldn't've": "would not have",
	"y'all": "you all",
	"y'all'd": "you all would",
	"y'all'd've": "you all would have",
	"y'all're": "you all are",
	"y'all've": "you all have",
	"you'd": "you had / you would",
	"you'd've": "you would have",
	"you'll": "you shall / you will",
	"you'll've": "you shall have / you will have",
	"you're": "you are",
	"you've": "you have"
	}
	for key, value in contractions.items():
		key= key.lower()
		value=value.lower()
	
	if type(x) is str:
		for key in contractions:
			value=contractions[key]
			x=x.replace(key,value)
		return x
	else:
		return x



# Removing Puntuation 
def _puntuation_removal(x):
	x=re.sub(r'[^\w]+', " ", x)
	return x

# converting to base form
def _make_to_base(x):
	x_list=[]
	doc=nlp(x)
	for token in doc:
		lemma=token.lemma_
		
		if lemma=='_PRON_' or lemma == 'be' or lemma == 'is': 
			lemma=token.text
			
		
		x_list.append(lemma)
	return ' '.join(x_list)

# Removing the emails
def _remove_emails(x):
	x= re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)
	return x

# Removing urls
def _remove_urls(x):
	x= re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)
	return x


# Creating tokens
def _tokenize(x):
	x= TextBlob(str(x)).words
	return x

# Remove stopwords
def _remove_stopwords(x):
	stopwords = ['a', 'about', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'but', 'by', 'can', \
			 'even', 'ever', 'for', 'from', 'get', 'had', 'has', 'have', 'he', 'her', 'hers', 'his', \
			 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'me', 'my', 'of', 'on', 'or', \
			 'see', 'seen', 'she', 'so', 'than', 'that', 'the', 'their', 'there', 'they', 'this', \
			 'to', 'was', 'we', 'were', 'what', 'when', 'which', 'who', 'will', 'with', 'you','-PRON-','pron']
	x = ' '.join([t for t in x.split() if t not in stopwords])
	return x