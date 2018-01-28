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

csv = 'tweet,label\n'

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    
    label = 'neutral'
    if analysis.sentiment.polarity > 0.2:
        label = 'positive'
    elif analysis.sentiment.polarity < -0.2:
        label = 'negative'

    csv += '"' + tweet.text + '",' + label + '\n'


with open("output.csv","w") as text_file:
    text_file.write(csv)

print("Saves result int output.csv")