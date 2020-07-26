import random
import requests
import xmltodict


class BlogPosts:

    def get(self):
        return_list = []
        response = requests.get('https://msadministrator.github.io/article/index.xml')
        data = xmltodict.parse(response.content)
        for item in data.get('rss').get('channel').get('item'):
            return_list.append(dict(item))
        return random.choice(return_list)
