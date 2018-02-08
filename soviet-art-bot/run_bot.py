import os
import tweepy

def twitter_api():
    access_token = settings.ACCESS_TOKEN
    access_token_secret = settings.ACCESS_SECRET
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    return api