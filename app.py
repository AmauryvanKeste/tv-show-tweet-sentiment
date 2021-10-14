import streamlit as st
import pandas as pd
import twint
from functions import preprocess
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import gunicorn

st.subheader("Check the popularity of a TV-show")
st.markdown("![SquidGame](https://media.giphy.com/media/8JCOK5E58CPxGfVJry/giphy.gif)")
# Collect Input from user :
tv_show = st.text_input("Enter the topic you are interested in (Press Enter once done)")
#num_tweets = st.slider("How many tweets would you like to analyse", 0, 1000, 40)
if len(tv_show) > 0:
    with st.spinner("Please wait, Tweets are being extracted"):
        c = twint.Config()
        c.Pandas = True
        c.Lang = "en"
        c.Limit = 1000
        c.Search = tv_show
        twint.run.Search(c)
        # result is saved to df
        df = twint.storage.panda.Tweets_df
    st.success('Tweets have been Extracted !!!!')
    df = df.drop_duplicates(subset=['id'], inplace=False)
    df = df[df['language'] == 'en']
    df.reset_index(inplace = True)
    df = df['tweet']
    df = df.apply(lambda x: preprocess(x))
    text = " ".join(tweet for tweet in df.astype(str))
    df['sentiment'] = df.apply(lambda x: TextBlob(x).sentiment[0])
    df['sentiment'] = df['sentiment'].apply(lambda x: "positive" if x > 0 else "negative" if x < 0 else ("neutral"))
    if st.button("See how many tweets were extracted"):
        # st.markdown(html_temp, unsafe_allow_html=True)
        st.success("Below is the number of extracted tweets :")
        st.write(df.size)
    if st.button("See the Extracted Data"):
        # st.markdown(html_temp, unsafe_allow_html=True)
        st.success("Below is the Extracted Data :")
        st.write(df.head(50))
    # Create and generate a word cloud image:
    if st.button("Get WordCloud for all things said about {}".format(tv_show)):
        st.success("Generating A WordCloud for all things said about {}".format(tv_show))
        text = " ".join(tweet for tweet in df.astype(str))
        wordcloud = WordCloud(max_words=800, max_font_size=70).generate(text)
        fig, ax = plt.subplots(1,1)
        plt.axis('off')
        plt.rcParams['figure.figsize'] = [20, 20]
        plt.tight_layout()
        st.write(plt.imshow(wordcloud, interpolation='bilinear'))
        st.pyplot(fig)
    # get the countPlot
    if st.button("Get Count Plot for Different Sentiments"):
        st.success("Generating A Count Plot")
        fig, ax = plt.subplots()
        st.subheader(" Count Plot for Different Sentiments")
        st.write(sns.countplot(df["sentiment"]))
        plt.xlabel('Sentiment',fontsize=20)
        plt.ylabel('Number of tweets', fontsize=20)
        plt.title("Countplot of tweet sentiment about {}".format(tv_show), fontsize=25)
        ax.tick_params(axis='x', which='major', labelsize=18)
        st.pyplot(fig)

    st.sidebar.header("About App")
    st.sidebar.info("A Twitter Sentiment analysis Project which will scrap twitter for the topic selected by the user. The extracted tweets will then be used to determine the Sentiments of those tweets. \
                    The different Visualizations will help us get a feel of the overall mood of the people on Twitter regarding the TV Show we select.")
    st.sidebar.text("Built with Streamlit")

    st.sidebar.header("For Any Queries/Suggestions Please reach out at :")
    st.sidebar.info("amaury.v.kesteren@gmail.com")
