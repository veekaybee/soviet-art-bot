"""
Connects to Twitter

"""
import tweepy

import settings

def twitter_api():
    access_token = settings.ACCESS_TOKEN
    access_token_secret = settings.ACCESS_SECRET
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)


    public_tweets = api.home_timeline()

    print("running...")

    for tweet in public_tweets:
        print(tweet.text)



twitter_api()