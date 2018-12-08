import tweepy
import pandas as pd
from textblob import TextBlob

consumer_key = 'Your_Key'
consumer_secret = 'Your_Key'
access_token = 'Your_Key'
access_token_secret = 'Your_Key'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweets = api.search('Evansville,IN')

textList = []
senitmentList = []

for t in tweets:
	txt = t.text
	textList.append(txt)
	analysis = TextBlob(txt)
	pol = analysis.sentiment.polarity
	if (pol > 0):
		senitmentList.append('Positive')
	else:
		senitmentList.append('Negative')

df = pd.DataFrame({'Tweet':textList, 'Sentiment':senitmentList})
df.to_csv('sentiment.csv', sep=',', encoding='utf-8')
