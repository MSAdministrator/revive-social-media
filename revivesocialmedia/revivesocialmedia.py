from .opensourceprojects import OpenSourceProjects
from .blogposts import BlogPosts
from .posttweet import PostTweet
from .postlinkedin import PostLinkedIn


class ReviveSocialMedia:

    _OSS_MESSAGE = 'OSS Project: {name} is {description}. Check it out! {url} #reviveposts'
    _BLOG_MESSAGE = 'Blog Post: {name}. Check it out! {url} #reviveposts'

    def blog(self):
        random_blog = BlogPosts().get()
        try:
            message = self._BLOG_MESSAGE.format(
                name=random_blog['title'],
                url=random_blog['link']
            )
            PostTweet().post(message)
        except:
            print("Error posting to Twitter")
            pass
        try:
            PostLinkedIn().post(
                message,
                random_blog['title'],
                random_blog['link']
            )
        except:
            print("Error posting to LinkedIn")
            pass
            #self.blog()

    def oss(self):
        random_project = OpenSourceProjects().get()
        tweet = self._OSS_MESSAGE.format(name=random_project['name'], description=random_project['description'], url=random_project['url'])
        try:
            if 'documentation' in random_project:
                tweet = tweet + ' Docs: {}'.format(random_project['documentation'])
            if 'repository' in random_project:
                tweet = tweet + ' Repo: {}'.format(random_project['repository'])
            if 'type' in random_project:
                tweet = tweet + ' #{}'.format(random_project['type'])
            PostTweet().post(tweet)
        except:
            print("Error posting to Twitter")
            pass
        try:
            PostLinkedIn().post(
                tweet, 
                random_project['name'],
                random_project['url']
            )
        except:
            print("Error posting to LinkedIn")
            pass
            #self.oss()
