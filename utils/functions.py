import streamlit as st
import pandas as pd
import re
import string
import emoji
import nltk
from nltk.tokenize import TweetTokenizer
from transformers import pipeline
from textblob import TextBlob

def give_sentiment_score(unique_tweet: str) -> str:
    new_tweet = expand_tweet(unique_tweet)
    analysis = TextBlob(new_tweet)
    return 'positive' if analysis.sentiment.polarity >= 0 else 'negative'

def expand_tweet(tweet: str) -> str:
    # general
    tweet = re.sub(r"n\'t", " not", tweet)
    tweet = re.sub(r"\'re", " are", tweet)
    tweet = re.sub(r"\'s", " is", tweet)
    tweet = re.sub(r"\'d", " would", tweet)
    tweet = re.sub(r"\'ll", " will", tweet)
    tweet = re.sub(r"\'t", " not", tweet)
    tweet = re.sub(r"\'ve", " have", tweet)
    tweet = re.sub(r"\'m", " am", tweet)
    # specific
    tweet = re.sub(r"won\'t", "will not", tweet)
    tweet = re.sub(r"can\'t", "can not", tweet)
    return tweet

def clean_user_topic(tweet: str) -> str:
    clean_user_text = ''
    for char in tweet:
        if char not in string.punctuation and not emoji.is_emoji(char) and char.isalpha():
            clean_user_text += char
    clean_user_text_no_space = clean_user_text.replace(' ', '')
    return clean_user_text_no_space

def preprocess(tweet: str) -> str:
    # lowercase tweet
    tweet = tweet.lower()

    # Defining regex patterns.
    urlPattern = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    urlpattern2 = r"(?:\@|http?\://|https?\://|www)\S+"
    userPattern = '@[^\s]+'
    alphaPattern = "\d+"
    sequencePattern = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"
    white_space_start_end = r"^\s+|\s+$"
    multiple_white_space = " +"
    retweet = r'^RT[\s]+'
    links = r'{link}'
    video = r'\[video\]'
    html_char = r'&[a-z]+;'

    tweet = re.sub(urlPattern, '', tweet)
    # Replace @USERNAME to ''.
    tweet = re.sub(userPattern, '', tweet)
    # Replace all non alphabets.
    tweet = re.sub(alphaPattern, "", tweet)
    # Replace 3 or more consecutive letters by 2 letter.
    tweet = re.sub(sequencePattern, seqReplacePattern, tweet)
    tweet = re.sub(white_space_start_end, "", tweet)
    tweet = re.sub(multiple_white_space, " ", tweet)
    tweet = re.sub(retweet, '', tweet)
    tweet = re.sub(links, '', tweet)
    tweet = re.sub(video, '', tweet)
    tweet = re.sub(html_char, '', tweet)

    return tweet
# function to remove punctuation and rare symbols

punct = list(string.punctuation)

def remove_punctuations(tweet: str) -> str:
    for punctuation in punct:
        tweet = tweet.replace(punctuation, '')
    return tweet

# function to convert emojis

def demojify(tweet: str) -> str:
    tweet = emoji.demojize(tweet, delimiters=(' ', ' '))
    return tweet

#function to limit the number of characters to fixed_n

def char_len(tweet: str, fixed_n: int) -> str:
    '''set string x to fixed_n character'''
    if len(tweet) > fixed_n:
        return tweet[:fixed_n]
    return tweet

# intantiate lemmatizer and tweettokenizer from NLTK

lemmatizer = nltk.WordNetLemmatizer()

tokenizer = TweetTokenizer(preserve_case=False,
                           strip_handles=True,
                           reduce_len=True)
# function to lemmatizer verbs and tokenize all words
def lemmatize_text(tweet: str) -> str:
    return [(lemmatizer.lemmatize(w, pos='v')) for w in tokenizer.tokenize((tweet))]

classifier = pipeline('sentiment-analysis')

def sentimenter(tweet: str) -> str:
    encoded_tweet = classifier(tweet)
    return encoded_tweet

# Converts df to csv
def convert_df(df: pd.Series):
    return df.to_csv().encode('utf-8')

