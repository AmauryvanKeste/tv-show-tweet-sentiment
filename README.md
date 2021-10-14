# Detecting the sentiment of a TV-show based on tweets
This was an individual project during our time at BeCode.
The aim of this project is to analyse tweets from on a TV-show in order to give an overall sentiment of that TV-show.
# Goal
1. Scrape at least 10000 tweets linked to a TV-show.
2. Using an existing model (transfer learning) analyse the tweets and give a sentiment
3. Create visualizations

# Link to the apps
[Heroku](https://twitter-sentiment-tv.herokuapp.com/)

[Streamlit.io](https://share.streamlit.io/amauryvankeste/tv-show-tweet-sentiment/main/app.py)

# Installation
## Python version
* Python 3.9.7

## Packages used
* textblob==0.15.3
* matplotlib==3.4.3
* streamlit==1.0.0
* wordcloud==1.8.1
* gunicorn==20.1.0
* nltk==3.6.5
* pandas==1.2.4
* seaborn==0.11.2
* twint==2.1.20
# Implementation
## Tweets
I first scrape tweets using the twint module which enables to bypass the official Twitter API and it's rate limits (3200 tweets).
Using twint I gather 10000 tweets in a few minutes.
## Preparing the data
The tweets scraped come in all languages so using pandas we focus on the english tweets only, dropping the other languages.
## Preprocessing
Using regex and nltk stopwords I remove the unncessary information from the tweets such as:
* "@username"
* "retweet"
* special characters such as: "!" and "#"
* alphanumeric characters
* all the tweets are lowercased
* stopwords are removed
## Sentiment
Using TextBlob I give a sentiment to each tweet where the choice is between "positive", "negative" and "neutral'.
## Deployment
The app is deployed on streamlit and on heroku.

The heroku app does not seem to work well because of twint issues.
## Visualizations
### WordCloud
Using WordCloud I generate a wordcloud based on the most common words in the tweets scraped:

![2021-10-14_14h37_36](https://user-images.githubusercontent.com/84380197/137319164-06ecd624-817e-475d-8038-f4ee26138782.png)

### Countplot
The user is able to generate a Countplot to obtain an overall sentiment of the TV-show:

![2021-10-14_14h38_43](https://user-images.githubusercontent.com/84380197/137319046-d3be5e3d-eb75-446a-85bd-4e709b1a970b.png)

The app also works for other keywords such as trump:

![2021-10-14_15h33_51](https://user-images.githubusercontent.com/84380197/137328857-0d3d30d5-b3d3-4084-9146-6fb78fae3782.png)


![2021-10-14_15h37_37](https://user-images.githubusercontent.com/84380197/137328863-fc138d28-69a0-458d-8c67-a063dfc569d5.png)

# Usage

## Main folder
| Folder            | Description                                                 |
|-------------------|-------------------------------------------------------------|
| Utils             | Directory containing the help functions                     |
| Graphs            | Directory containing all graphs                             |


# Author
| Name                   | Github                              |
|------------------------|-------------------------------------|
| Amaury van Kesteren    | https://github.com/AmauryvanKeste   |




# Timeline
11/10/2021 - 14/10/2021
