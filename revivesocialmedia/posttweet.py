import os
import requests
from bs4 import BeautifulSoup, Tag
import tweepy
import random


class PostTweet(object):

    __twitter_consumer_key = os.environ.get('TWITTER_TOKEN')
    __twitter_secret_key = os.environ.get('TWITTER_SECRET_KEY')
    __twitter_access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    __twitter_access_secret = os.environ.get('TWITTER_ACCESS_SECRET')

    def __post_to_twitter(self, message):
        auth = tweepy.OAuthHandler(self.__twitter_consumer_key, self.__twitter_secret_key)
        auth.set_access_token(self.__twitter_access_token, self.__twitter_access_secret)
        self.api = tweepy.API(auth)
        self.api.update_status(message)

    def post(self, message):
        auth = tweepy.OAuthHandler(self.__twitter_consumer_key, self.__twitter_secret_key)
        auth.set_access_token(self.__twitter_access_token, self.__twitter_access_secret)
        self.api = tweepy.API(auth)
        self.api.update_status(message)
