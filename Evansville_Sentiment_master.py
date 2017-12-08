import tweepy
import pandas as pd
from textblob import TextBlob

consumer_key = 'b4SNz9obyzqOB3wp5JjSFJmqV'
consumer_secret = 'Hata6pwURRaTf2YfeDUpcOEnV3X1nxpDttyGqScCisuwN8G4fE'

access_token = '732828479805378560-s7mI9G1ooDm7AtFpHk798NteP7lpKFE'
access_token_secret = 'zQAuq4YLVziB7iS7ICixyo0mHk41ZzgUKGL3PcZ0fipa7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Evansville, Indiana')

textList = list()
senitmentList = list()


# create a For-Loop to go through all tweets assesing Evansville
for tweet in public_tweets: 
	txt = tweet.text
	textList.append(txt)
	analysis = TextBlob(txt)
	pol = analysis.sentiment.polarity
	if (pol > 0):
		senitmentList.append('Positive')
	else: 
		senitmentList.append('Negative')


df = pd.DataFrame({'Tweet':textList, 'Sentiment':senitmentList})
df.to_csv('sentiment.csv', sep=',', encoding='utf-8')