"""
Connects to Twitter

"""
import tweepy


import settings

def access_twitter_api():
    access_token = settings.ACCESS_TOKEN
    access_token_secret = settings.ACCESS_SECRET
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api

def post_tweet(api):
    api.update_with_media('/Users/vboykis/Desktop/soviet-art-bot/assetsyouth-of-the-poetess-1967.jpg', status="\"Youth of the poetess\"\nPainter, 1967")
    print("Tweet posted")


api = access_twitter_api()
post_tweet(api)
