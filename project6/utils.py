from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
import string
import re
import numpy as np

def process_tweet(tweet):
    stemmer=PorterStemmer()
    stopwords_english=stopwords.words('english')
    
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)
    
    tokenizer=TweetTokenizer(preserve_case=False,strip_handles=True,
                             reduce_len=True)
    
    tweet_tokens=tokenizer.tokenize(tweet)
    
    tweets_clean=[]
    
    for word in tweet_tokens:
        if word not in stopwords_english and\
            word not in string.punctuation:
            stem_word=stemmer.stem(word)
            tweets_clean.append(stem_word)
    
    return tweets_clean



def get_document_embedding(tweet,en_embeddings):    
    '''
    Input:
        - tweet: a string
        - en_embeddings: a dictionary of word embeddings
    Output:
        - tweet_embedding: a
    '''
    
    doc_embedding=np.zeros(300)
    
    processed_doc=process_tweet(tweet)
    
    for word in processed_doc:
        doc_embedding+=en_embeddings.get(word,0)
        
    return doc_embedding