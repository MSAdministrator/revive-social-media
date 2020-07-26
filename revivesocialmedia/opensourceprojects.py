import requests
from bs4 import BeautifulSoup, Tag
import random


class OpenSourceProjects(object):

    _URL = 'https://letsautomate.it/page/open-source-projects/'
    _PROJECT_LIST = []

    def get(self):
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
        return random.choice(self._PROJECT_LIST)
