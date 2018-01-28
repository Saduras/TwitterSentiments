import tweepy
from textblob import TextBlob

consumer_key = 'DX18Qbrjs5MGvOqc1Ip26eAx6'
consumer_secret = 'aafMFAiCxF4xwFxaHrL12iEDzZrJkSX585zi9dgnAc7LWNc6el'

access_token = '3298406491-G7meLdQF1e7Z3RjykJmSuAbkZ79mkur8Wsw8wuM'
access_token_secret = 'nO1ng9F5IgiX2moY6GXR7x9zNjoEfw1n77XWs5zaBXOkP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment, '\n')