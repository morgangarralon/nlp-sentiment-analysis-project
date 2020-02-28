from app import app
from twitter import OAuth, Twitter
from app.models.DataInputApi import DataInputApi

class DataInputTwitter(DataInputApi):
    def __init__(self):
        super().__init__("twitter")
        access_token = app.config['TWITTER_ACCESS_TOKEN']
        access_secret = app.config['TWITTER_ACCESS_SECRET']
        consumer_key = app.config['TWITTER_API_KEY']
        consumer_secret = app.config['TWITTER_API_SECRET']
        auth = OAuth(access_token, access_secret, consumer_key, consumer_secret)
        self.api = Twitter(auth=auth)

        print(self.api)

    def getData(self, keyword, count=1):
        result = self.api.search.tweets(q=keyword, count=count, lang='en', include_entities=False)

        return result['statuses'][0]['text']

    