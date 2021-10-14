import re
import string

def preprocess(tweet):
    # Defining regex patterns.
    urlPattern = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    userPattern = '@[^\s]+'
    alphaPattern = "\d+"
    sequencePattern = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"

    # lowercase tweet
    tweet = tweet.lower()

    #Replace @USERNAME to ''.
    tweet = re.sub(userPattern, '', tweet)
    # Replace all non alphabets.
    tweet = re.sub(alphaPattern, "", tweet)
    # Replace 3 or more consecutive letters by 2 letter.
    tweet = re.sub(sequencePattern, seqReplacePattern, tweet)
    #tweet = [w for w in tweet if not w in stop]
    tweet = "".join([char for char in tweet if char not in string.punctuation])

    return tweet