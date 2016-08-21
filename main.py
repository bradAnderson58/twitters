# import webapp2
# import logging

# import json
# import sys
import tweepy
# import calendar
import ConfigParser
# import HTMLParser

from tweepy import *

class Util:

  @staticmethod
  def randomInt(max):
    return random.randint(0, max)

  @staticmethod
  def copyArrayOfArrays(arr):
    result = []
    for innerArray in arr:
      result.append(innerArray)

    return result

# end Util class

class BullShit:
  sentencePool = []

  @staticmethod
  def initSentencePool():
    sentencePool = Util.copyArrayOfArray(sentencePatterns)


# end BullShit class


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

def generateSentence(topic):
  x = 0
  # choose a pattern number
  patternNum = Util.randomInt(BullShit.sentencePool[topic].length - 1)
  print patternNum

  # get the pattern
  pattern = BullShit.sentencePool[topic][patternNum]
  print pattern




#tweet('test3!')

