import os
import requests
from bs4 import BeautifulSoup, Tag
import tweepy
import random

class TwitterPost(object):

    _URL = 'https://letsautomate.it/page/open-source-projects/'
    _PROJECT_LIST = []
    _TWEET = 'OSS Project: {name} is {description}. Check it out! {url}'

    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret
        

    def get_data(self):
        response = requests.get(self._URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        section = soup.find('span').parent
        for ul_tag in soup.find_all('ul'):
            for li in ul_tag.find_all('li'):
                if li.text not in ['Open Source Projects', 'Presentations', 'About']:
                    if li and li.a:
                        return_dict = {}
                        if 'http' not in li.a.text:
                            return_dict['name'] = li.a.text
                            return_dict['url'] = li.a['href']
                        for l in li.find_all('li'):
                            if 'Type:' in l.text:
                                return_dict['type'] = l.text.replace('Type:','').strip()
                            elif 'Documentation:' in l.text:
                                return_dict['documentation'] = l.text.replace('Documentation:','').strip()
                            elif 'Package Repository:' in l.text:
                                return_dict['repository'] = l.text.replace('Package Repository:','').strip()
                            else:
                                return_dict['description'] = l.text
                        if return_dict:
                            self._PROJECT_LIST.append(return_dict)


    def post(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token_key, self.access_token_secret)
        self.api = tweepy.API(auth)
        if not self._PROJECT_LIST:
            self.get_data()
        random_project = random.choice(self._PROJECT_LIST)
        try:
            tweet = self._TWEET.format(name=random_project['name'], description=random_project['description'], url=random_project['url'])
            if 'documentation' in random_project:
                tweet = tweet + ' Docs: {}'.format(random_project['documentation'])
            if 'repository' in random_project:
                tweet = tweet + ' Repo: {}'.format(random_project['repository'])
            if 'type' in random_project:
                tweet = tweet + ' #{}'.format(random_project['type'])

            self.api.update_status(tweet)
        except:
            self.post()


tweet = TwitterPost(
    os.environ['TWITTER_TOKEN'],
    os.environ['TWITTER_SECRET_KEY'], 
    os.environ['TWITTER_ACCESS_TOKEN'], 
    os.environ['TWITTER_ACCESS_SECRET'])
tweet.post()