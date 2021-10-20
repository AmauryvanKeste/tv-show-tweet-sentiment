______________________________________________________________________________________________________________________________________________________
![Twitter](https://user-images.githubusercontent.com/84380197/138159713-08f1cf0d-e036-4111-a083-b8e6aab11582.jpg)
______________________________________________________________________________________________________________________________________________________


- Developer Name: `Amaury van Kesteren`
- Level: `Junior Data Scientist`
- Duration: `4 days`
- Deadline : `14/10/21 4:00 PM`
- Team challenge: `Solo project`
- Type of challenge: `Learning`
- Promotion : `AI ARAI 2.31`
- Coding Bootcamp: `Becode Artificial Intelligence (AI) Bootcamp`

## Mission Objectives

1. Scrape at least 10000 tweets linked to a TV-show.
2. Using an existing model (transfer learning) analyse the tweets and give a sentiment
3. Create visualizations

____________________________________________________________________________________________________________________________________________

## About The Repository

This is a project about developing a Natural language processing model that is able to give a sentiment on a tweet.

The task is to:
1. Give a sentiment on an individual sentiment.
2. Create a script that is able to 'live' scrape and give an overall sentiment on a topic.
3. Create a script to clean the tweets to enable more accurate sentiment analysis.
4. Create visuals giving a clear idea of the overall sentiment.


**Search bars tab where you search for the sentiment of one tweet and the BERT and TextBlob NLP models will return a positive, neutral or negative sentiment.**

![image](https://user-images.githubusercontent.com/84380197/138159889-82cadc9e-563f-4d72-b9aa-07ff8357d1a8.png)

**Sample Search bar tab where you search for the overall sentiment of on specified topic and the BERT and TextBlob NLP models will return a positive, neutral or negative sentiment.**

Using WordCloud I generate a wordcloud based on the most common words in the tweets scraped:

![2021-10-14_14h37_36](https://user-images.githubusercontent.com/84380197/137319164-06ecd624-817e-475d-8038-f4ee26138782.png)

The user is able to generate a Countplot to obtain an overall sentiment of the TV-show:

![2021-10-14_14h38_43](https://user-images.githubusercontent.com/84380197/137319046-d3be5e3d-eb75-446a-85bd-4e709b1a970b.png)

The app also works for other keywords such as trump:

![2021-10-14_15h33_51](https://user-images.githubusercontent.com/84380197/137328857-0d3d30d5-b3d3-4084-9146-6fb78fae3782.png)


![2021-10-14_15h37_37](https://user-images.githubusercontent.com/84380197/137328863-fc138d28-69a0-458d-8c67-a063dfc569d5.png)

____________________________________________________________________________________________________________________________________________

## Link to the apps

____________________________________________________________________________________________________________________________________________

## R E P O S I T O R Y

**README.md**
  - has all the necessary information regarding the project

**app.py**
  - Streamlit app containing the code for deploying.
  - Deploying is done on streamlit.io and Heroku

**Procfile**
  - Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
  - This Procfile is used to declare a variety of process types, including: the app's web server.

**requirements.txt**
  - is a txt file used for specifying what python packages are required to run this project

**assets folder**
  - this is where the picture is stored

**utils folder**
  - this is where the functions are stored.
______________________________________________________________________________________________________________________________________________________

## Libraries Used For This Project

**Hugging Face 🤗 Transformers**  https://huggingface.co/transformers/
  - Hugging Face is an NLP-focused startup with a large open-source community, in particular around the Transformers library. 
  - 🤗 Transformers is a python-based library that exposes an API to use many well-known transformer architectures, such as BERT, RoBERTa, GPT-2 or DistilBERT, that obtain state-of-the-art results on a variety of NLP tasks like text classification, information extraction, question answering, and text generation. 
  - Those architectures come pre-trained with several sets of weights. 
  - In this project, transformers pipeline is used to summarize the text

**TextBlob** https://flask.palletsprojects.com/en/1.1.x/
  - TextBlob is a Python (2 and 3) library for processing textual data. 
  - It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis and more.

**Pandas** https://pypi.org/project/pandas/
  - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
  - In this project, pandas is used convert a list to create a dataframe 

**Heroku** //www.heroku.com
  - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
  - In this project, Heroku is used to deploy the app but due to limited GB since we are only using the free version, it was returning an error that the slug size is too big.
  - As free users of Heroku, we are only allowed of up to 500MB slug size.
  - Everything is already in the repository, the Procfile and the requirements.txt, we just need a bigger slug size to deploy it
  
 **Streamlit** //https://streamlit.io/
  - The fastest way to build and share data apps
  - Streamlit turns data scripts into shareable web apps in minutes. 
______________________________________________________________________________________________________________________________________________________

## Clone / Fork This Repository
  - If you wish to clone/fork this repository, you can just click on the repository, then click the Clone/fork button and follow the instructions.

![Thank you](https://user-images.githubusercontent.com/84380197/138157253-af820ee0-5cea-4ef2-8d80-cbba993c5026.jpg)
### Thank you for reading. Have fun with the code! 🤗
