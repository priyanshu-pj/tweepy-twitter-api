import tweepy
import configparser

config = configparser.RawConfigParser()
config.read('config.ini')

API_KEY = config['twitter']['API_KEY']
API_KEY_SECRET = config['twitter']['API_KEY_SECRET']
ACCESS_TOKEN = config['twitter']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['twitter']['ACCESS_TOKEN_SECRET']
BEARER_TOKEN = config['twitter']['BEARER_TOKEN']
CLIENT_ID = config['twitter']['CLIENT_ID']
CLIENT_SECRET = config['twitter']['CLIENT_SECRET']

## Twitter API v1.1

# # Authentication with OAuth2.0 Bearer Token
# auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
# api = tweepy.API(auth)

# # Authentication with OAuth2AppHandler
# auth = tweepy.OAuth2AppHandler(API_KEY, API_KEY_SECRET)
# api = tweepy.API(auth)

# # Authentication with OAuth1UserHandler
# auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

## Twitter API v2.0

# # Authentication with OAuth2.0 Bearer Token
# client = tweepy.Client(BEARER_TOKEN)

# # Authentication with OAuth1.0
# client = tweepy.Client(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# # OAuth2UserHandler
# client = tweepy.Client(CLIENT_ID, 'https://github.com/priyanshu87694', CLIENT_SECRET)
