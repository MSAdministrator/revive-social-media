import os
import json, requests
from .browser import Browser


class PostLinkedIn(object):

    __URL = 'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={client_id}&redirect_uri={url}&state=fooobar&scope=r_liteprofile%20r_emailaddress%20w_member_social'
    __auth_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    __request_url = 'https://api.linkedin.com/'
    __redirect_uri='http://google.com'
    __authorization_code = None
    __profile = None

    def __init__(self):
        self.__linkedin_client_id = os.environ['LINKEDIN_CLIENT_ID']
        self.__linkedin_client_secret = os.environ['LINKEDIN_CLIENT_SECRET']
        self.__linkedin_username = os.environ['LINKEDIN_USERNAME']
        self.__linkedin_password = os.environ['LINKEDIN_PASSWORD']
        self.__access_token = os.environ.get('LINKEDIN_ACCESS_TOKEN')

    def __get_access_token(self):
        browser = Browser(self.__linkedin_username, self.__linkedin_password)
        authorization_code = browser.run(self.get_authorization_url())
        self.authorization_code_flow(authorization_code)

    def get_authorization_url(self):
        return self.__URL.format(
            client_id=self.__linkedin_client_id,
            url=self.__redirect_uri
        )

    def authorization_code_flow(self, authorization_code):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': self.__redirect_uri,
            'client_id': self.__linkedin_client_id,
            'client_secret': self.__linkedin_client_secret
        }
        response = requests.post(self.__auth_url, params=body, headers=headers).json()
        self.__access_token = response['access_token']

    def client_credential_code_flow(self):
        pass
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.__linkedin_client_id,
            'client_secret': self.__linkedin_client_secret
        }
        return requests.post(
            url=self.__auth_url, 
            params=body, 
            headers=headers
        ).json()

    def get_profile(self):
        return requests.get(
            url=self.__request_url + 'v2/me', 
            headers={'Authorization': 'Bearer {token}'.format(token=self.__access_token)}
        ).json()

    def post(self, main_body, article_text, article_link, media_category='ARTICLE'):
        if not self.__access_token:
            self.__get_access_token()
        endpoint = 'v2/ugcPosts'
        if not self.__profile:
            self.__profile = self.get_profile()
        body = {
            'author': "urn:li:person:{}".format(self.__profile.get('id')),
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": main_body
                    },
                    "shareMediaCategory": media_category,
                    "media": [
                        {
                            "status": "READY",
                            "description": {
                                "text": article_text
                            },
                            "originalUrl": article_link,
                            "title": {
                                "text": article_text
                            }
                        }
                    ]
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        return requests.post(
            url=self.__request_url + endpoint, 
            json=body, 
            headers={'Authorization': 'Bearer {token}'.format(token=self.__access_token)}
        ).json()
