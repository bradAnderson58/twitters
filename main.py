import tweepy
import ConfigParser
import patterns
import random
import re
import vocab

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
  sentencePool = Util.copyArrayOfArrays(patterns.sentencePatterns)
  words = vocab.words

# end BullShit class

def retrieveRandomWordOfType(ty):
  rand = Util.randomInt(len(BullShit.words[ty]) - 1)
  return BullShit.words[ty][rand]

# Update the Twitter account authorized
# in settings.cfg with a status message
def tweet(status):
  config = ConfigParser.RawConfigParser()
  config.read('settings.cfg')

  # http://apps.twitter.com/apps/<id>/keys
  CONSUMER_KEY = config.get('Twitter OAuth', 'CONSUMER_KEY')
  CONSUMER_SECRET = config.get('Twitter OAuth', 'CONSUMER_SECRET')
  ACCESS_TOKEN_KEY = config.get('Twitter OAuth', 'ACCESS_TOKEN_KEY')
  ACCESS_TOKEN_SECRET = config.get('Twitter OAuth', 'ACCESS_TOKEN_SECRET')

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)
  result = api.update_status(status)

def generateSentence(topic):

  # choose a pattern number
  patternNum = Util.randomInt(len(BullShit.sentencePool[topic]) - 1)
  # get the pattern
  pattern = BullShit.sentencePool[topic][patternNum]

  # insert space before punctuations to split into array
  pattern = re.sub(r"([\.,;\?])", ' \\1', pattern)
  pattern = pattern.split(' ')

  result = ''
  for word in pattern:
    # if word matches a placeholder word, replace with random instance
    if word in BullShit.words:
      result += retrieveRandomWordOfType(word)
    else:
      result += word
    result += ' '

  # replace 'a [vowel]' with 'an [vowel]'
  result = re.sub(r"(^|\W)([Aa]) ([aeiou])", '\\1\\2n \\3', result)

  result = result.strip()
  result = result.capitalize()

  # remove spaces before commas and such
  result = re.sub(r" ([,\.;\?])", '\\1', result)
  # remove space before hyphens in prefixes
  result = re.sub(r"(\w-) ", '\\1', result)
  # add spaces after question marks if they mid sentence
  result = re.sub(r"\?(\w)", '? \\1', result)

  return result

mTweet = generateSentence(Util.randomInt(len(BullShit.sentencePool) - 1))

#print mTweet
tweet(mTweet)

