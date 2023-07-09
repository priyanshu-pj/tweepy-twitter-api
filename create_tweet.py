import tweepy
import configparser

config = configparser.RawConfigParser()
config.read('config.ini')

API_KEY = config['twitter']['API_KEY']
API_KEY_SECRET = config['twitter']['API_KEY_SECRET']
ACCESS_TOKEN = config['twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['twitter']['ACCESS_TOKEN_SECRET']
BEARER_TOKEN = config['twitter']['BEARER_TOKEN']

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# not essential, helpful for older tweepy version
# auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# create tweet
client.create_tweet(text='Hello World 2')
