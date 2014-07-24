from config import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

from twython import Twython, TwythonError
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import random

array = []
arrayto = []
arraytc = []
arrayhn = []
arrayph = []
randomt = ""


# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
techcrunch = twitter.get_user_timeline(screen_name='techcrunch', count=20, include_rts=False)
for tweet in techcrunch:
    tweet = tweet['text'] + "\n"
    p = tweet.find("htt")
    tweet = tweet[:p]
    tweet = tweet.encode('utf-8')
    arraytc.append(tweet)

producthunt = twitter.get_user_timeline(screen_name='producthunt', count=20, include_rts=False)
for tweet in producthunt:
    tweet = tweet['text'] + "\n"
    p = tweet.find("htt")
    tweet = tweet[:p]
    tweet = tweet.encode('utf-8')
    arrayph.append(tweet)


onion = twitter.get_user_timeline(screen_name='theonion', count=20, include_rts=False)
for tweet in onion:
    tweet = tweet['text'] + "\n"
    p = tweet.find("htt")
    tweet = tweet[:p]
    tweet = tweet.encode('utf-8')
    arrayto.append(tweet)

hackernews = twitter.get_user_timeline(screen_name='newsycombinator', count=20, include_rts=False)
for tweet in hackernews:
    tweet = tweet['text'] + "\n"
    p = tweet.find("htt")
    tweet = tweet[:p]
    tweet = tweet.encode('utf-8')
    arrayhn.append(tweet)