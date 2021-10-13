import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
from emoji_translate.emoji_translate import Translator

emo = Translator(exact_match_only=False, randomize=True)

emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad',':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed',':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused',
          '$_$': 'greedy','@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused','<(-_-)>': 'robot', 'd[-_-]b': 'dj',
          ":'-)": 'sadsmile',';)': 'wink',';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}

def preprocess(tweet):
    # Defining regex patterns.
    urlPattern = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    userPattern = '@[^\s]+'
    alphaPattern = "\d+"
    sequencePattern = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"

    tweet = tweet.lower()

    # Repace all URls with 'URL'
    tweet = re.sub(urlPattern, '', tweet)
    # Replace all emojis.
    #tweet = emo.demojify(tweet)
    #for emoji in emojis.keys():
        #tweet = tweet.replace(emoji, "EMOJI" + emojis[emoji])
    #Replace @USERNAME to 'USER'.
    tweet = re.sub(userPattern, '', tweet)
    # Replace all non alphabets.
    tweet = re.sub(alphaPattern, "", tweet)
    # Replace 3 or more consecutive letters by 2 letter.
    tweet = re.sub(sequencePattern, seqReplacePattern, tweet)
    #tweet = [w for w in tweet if not w in stop]
    tweet  = "".join([char for char in tweet if char not in string.punctuation])
    # tweetwords = ''
    # for word in tweet.split():
    #     if len(word) > 1:
    #         # Lemmatizing the word.
    #         word = wordLemm.lemmatize(word)
    #         tweetwords += (word + ' ')

    return tweet