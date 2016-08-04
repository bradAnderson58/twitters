import webapp2
import logging

import json
import sys
import tweepy
import calendar
import ConfigParser
import HTMLParser

from tweepy import *
from ConfigParser import NoSectionError, NoOptionError
from time import gmtime, strftime
from urllib2 import urlopen, URLError
from zlib import decompress, MAX_WBITS

HOURS = 8
MAX_TWEET_LEN = 140
DATE_FORMAT = "%Y %b %d %H:%M:%S UTC"

# Update the Twitter account authorized
# in settings.cfg with a status message
def tweet(status):
  config = ConfigParser.RawConfigParser()
  config.read('settings.cfg')

  # http://apps.twitter.com/apps/12687042/keys
  CONSUMER_KEY = config.get('Twitter OAuth', 'CONSUMER_KEY')
  CONSUMER_SECRET = config.get('Twitter OAuth', 'CONSUMER_SECRET')
  ACCESS_TOKEN_KEY = config.get('Twitter OAuth', 'ACCESS_TOKEN_KEY')
  ACCESS_TOKEN_SECRET = config.get('Twitter OAuth', 'ACCESS_TOKEN_SECRET')

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)
  result = api.update_status(status)

  print result



tweet('hello world')

