import streamlit as st
from PIL import Image
from transformers import pipeline
import twint
from utils.functions import *
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Tweet Sentiment analysis app",
    layout='centered')
image = Image.open('assets/twitter.jpeg')
st.image(image, width=800)
st.write('---')


# make container:
header = st.container()

# Sidebar modules
st.sidebar.title('Menu Bar')
user_selection = st.sidebar.selectbox('Choose the module', options = ['Individual tweet sentiment','Tweet overall sentiment'])

# Sidebar info
st.sidebar.info("A Twitter Sentiment analysis Project which will scrape Twitter for the topic selected by the user. The extracted tweets will then be used to determine the Sentiments of those tweets. \
                The different Visualizations will help us get a feel of the overall mood of the people on Twitter regarding the topic the user selects.")
st.sidebar.info("Built with Streamlit, Twint, BERT (Hugging Face), TextBlob")
st.sidebar.text("Ideas for new projects ?! :")
st.sidebar.info("Reach out @ amaury.v.kesteren@gmail.com !")

if user_selection == "Individual tweet sentiment":
    with header:
        st.subheader("Check the sentiment of your next tweet with TextBlob")

        form = st.form(key='form-TextBlob')
        unique_tweet = form.text_input('Enter your tweet')
        submit_1 = form.form_submit_button('Go')
        if submit_1:
            response_unique_tweet = give_sentiment_score(unique_tweet)
            st.write("Your tweet is: ", response_unique_tweet)

        st.subheader("Check the sentiment of your next tweet with BERT")
        my_expander = st.expander(label='Expand me if you would like to meet BERT (an advanced NLP tool)')
        with my_expander:
            form = st.form(key='form-BERT')
            unique_tweet_bert = form.text_input('Enter your tweet')
            submit = form.form_submit_button('Go')
            if submit:
                with st.spinner("Please wait, your tweet is being analysed"):
                    classifier = pipeline("sentiment-analysis")
                    result = classifier(unique_tweet_bert)[0]
                    label = result['label']
                    score = round(result['score'], 2)
                    if label == 'POSITIVE':
                        st.success(f'Your tweet gives a {label} sentiment (score: {score})')
                    else:
                        st.error(f'Your tweet gives a {label} sentiment (score: {score})')

elif user_selection == "Tweet overall sentiment":
    with header:
        st.title("This module analyses overall sentiment")

        # Collect Input from user :
        form = st.form(key='form-overall-sentiment')
        input_tag = form.text_input("Enter the topic (in English) you are interested in (Press Go)")
        submit_2 = form.form_submit_button('Go')

        # Slider gives the number of tweets that the user wants to analyse
        num_tweets = st.slider("How many tweets would you like to analyse (The more, the longer the scraping)"
                               " and processing time", 0, 1000, 40)
        if len(input_tag) > 0:
            with st.spinner("Please wait, Tweets are being extracted"):
                st.write(
                    f"*Summary:* {str(num_tweets)} tweets about __{input_tag}__ are being scraped and analyzed.")
                input_tag_cleaned = clean_user_topic(input_tag)
                c = twint.Config()
                c.Pandas = True
                c.Lang = "en"
                c.Limit = round(num_tweets*1.5)
                c.Search = input_tag_cleaned
                twint.run.Search(c)
                # result is saved to df
                df = twint.storage.panda.Tweets_df
            st.success('Tweets have been Extracted !!!!')

            with st.spinner("Please wait, Tweets are being cleaned 🧹 😃 🧹"):
                # prepare the data by dropping all other languages
                df = df[df['language'] == 'en']
                # reset index
                df.reset_index(inplace=True)
                # drop useless columns
                df = df.drop(columns = ['index', 'id', 'conversation_id', 'created_at', 'date', 'time', 'timezone',
                   'user_id', 'username', 'name', 'place', 'language', 'mentions',
                   'urls', 'photos', 'replies_count', 'retweets_count', 'likes_count',
                   'hashtags', 'cashtags', 'link', 'retweet', 'quote_url', 'video',
                   'thumbnail', 'near', 'geo', 'source', 'user_rt_id', 'user_rt',
                   'retweet_id', 'reply_to', 'retweet_date', 'translate', 'trans_src',
                   'trans_dest'])

                df['clean'] = df['tweet'].apply(lambda x: expand_tweet(x))
                # apply the preprocess function to clean the data
                df['clean'] = df['clean'].apply(lambda x: preprocess(x))

                # remove the punctuation with a function
                df["clean"] = df["clean"].apply(lambda x: remove_punctuations(x))

                # convert the emojos into readable strings
                df["clean"] = df["clean"].apply(lambda x: demojify(x))

                # limit the number of characters
                df['clean'] = df['clean'].apply(lambda x: char_len(x, 255))

                # apply NLTK lemmatizer and tokenizer
                df['clean'] = df['clean'].apply(lambda x: lemmatize_text(x))

                # remove stopwords based on NLTK's english list of stopwords
                stop_words = set(stopwords.words('english'))
                df["clean"] = df["clean"].apply(lambda x: [item for item in x if item not in stop_words])

                st.success('Tweets have been Cleaned !!!!')

            with st.spinner("Calculating sentiment ... "):
                df['sentiment'] = df['clean'].apply(lambda x: TextBlob(' '.join(x)).sentiment[0])
                df['sentiment'] = df['sentiment'].apply(lambda x: "positive" if x > 0 else "negative" if x < 0 else ("neutral"))

                st.success('Tweets have been Scored !!!!')
                st.write(df)
                csv = convert_df(df)
                st.write('')

                # build the streamlit features
                # get the countPlot
                if st.button("Get histogram for Different Sentiments"):
                    st.success("Generating A Count Plot")
                    fig = px.histogram(df, x=df.sentiment)
                    fig.update_layout(title_text="Countplot of tweet sentiment about {}".format(input_tag))
                    fig.update_xaxes(title_text='Sentiment')
                    fig.update_yaxes(title_text='Number of tweets')
                    fig.update_layout(bargap=.1)
                    st.plotly_chart(fig)

                # Create and generate a word cloud image:
                if st.button("Get WordCloud for all things said about {}".format(input_tag)):
                    st.success("Generating A WordCloud for all things said about {}".format(input_tag))
                    text = " ".join(tweet for tweet in df['tweet'].astype(str))
                    wordcloud = WordCloud(max_words=800, max_font_size=70).generate(text)
                    fig, ax = plt.subplots(1, 1)
                    ax.imshow(wordcloud, interpolation='bilinear')
                    ax.axis('off')
                    st.pyplot(fig)

                # Downloads dataframe as csv if button push
                col1, col2, col3 = st.columns(3)
                col1.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='Twitter_scraped_data.csv',
                    mime='text/csv')

