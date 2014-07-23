from config import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

from twython import Twython, TwythonError
import random

array = []
randomt = ""


# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
techcrunch = twitter.get_user_timeline(screen_name='techcrunch', include_rts=None, count=7)
for idx, tweet in enumerate(techcrunch):
    if idx == 0:
    	tweet1tc = tweet['text'] + "\n"
    	p = tweet1tc.find("htt")
    	tweet1tc = tweet1tc[:p]
    if idx == 1:
    	tweet2tc = tweet['text'] + "\n"
    	p = tweet2tc.find("htt")
    	tweet2tc = tweet2tc[:p]
    if idx == 2:
    	tweet3tc = tweet['text'] + "\n"
    	p = tweet3tc.find("htt")
    	tweet3tc = tweet3tc[:p]
    if idx == 3:
    	tweet4tc = tweet['text'] + "\n"
    	p = tweet4tc.find("htt")
    	tweet4tc = tweet4tc[:p]
    if idx == 4:
    	tweet5tc = tweet['text'] + "\n"
    	p = tweet5tc.find("htt")
    	tweet5tc = tweet5tc[:p]
    if idx == 5:
    	tweet6tc = tweet['text'] + "\n"
    	p = tweet6tc.find("htt")
    	tweet6tc = tweet6tc[:p]
    if idx == 6:
    	tweet7tc = tweet['text'] + "\n"
    	p = tweet7tc.find("htt")
    	tweet7tc = tweet7tc[:p]


    #print tweet['text'] + "\n"

producthunt = twitter.get_user_timeline(screen_name='producthunt', include_rts=None, count=7)
for idx, tweet in enumerate(producthunt):
    if idx == 0:
    	tweet1ph = tweet['text'] + "\n"
    	p = tweet1ph.find("htt")
    	tweet1ph = tweet1ph[:p]
    if idx == 1:
    	tweet2ph = tweet['text'] + "\n"
    	p = tweet2ph.find("htt")
    	tweet2ph = tweet2ph[:p]
    if idx == 2:
    	tweet3ph = tweet['text'] + "\n"
    	p = tweet3ph.find("htt")
    	tweet3ph = tweet3ph[:p]
    if idx == 3:
    	tweet4ph = tweet['text'] + "\n"
    	p = tweet4ph.find("htt")
    	tweet4ph = tweet4ph[:p]
    if idx == 4:
    	tweet5ph = tweet['text'] + "\n"
    	p = tweet5ph.find("htt")
    	tweet5ph = tweet5ph[:p]
    if idx == 5:
    	tweet6ph = tweet['text'] + "\n"
    	p = tweet6ph.find("htt")
    	tweet6ph = tweet6ph[:p]
    if idx == 6:
    	tweet7ph = tweet['text'] + "\n"
    	p = tweet7ph.find("htt")
    	tweet7ph = tweet7ph[:p]


onion = twitter.get_user_timeline(screen_name='theonion', include_rts=None, count=7)
for idx, tweet in enumerate(onion):
    if idx == 0:
        tweet1to = tweet['text'] + "\n"
        p = tweet1to.find("htt")
        tweet1to = tweet1to[:p]
    if idx == 1:
        tweet2to = tweet['text'] + "\n"
        p = tweet2to.find("htt")
        tweet2to = tweet2to[:p]
    if idx == 2:
        tweet3to = tweet['text'] + "\n"
        p = tweet3to.find("htt")
        tweet3to = tweet3to[:p]
    if idx == 3:
        tweet4to = tweet['text'] + "\n"
        p = tweet4to.find("htt")
        tweet4to = tweet4to[:p]
    if idx == 4:
    	tweet5to = tweet['text'] + "\n"
    	p = tweet5to.find("htt")
    	tweet5to = tweet5to[:p]
    if idx == 5:
    	tweet6to = tweet['text'] + "\n"
    	p = tweet6to.find("htt")
    	tweet6to = tweet6to[:p]
    if idx == 6:
    	tweet7to = tweet['text'] + "\n"
    	p = tweet7to.find("htt")
    	tweet7to = tweet7to[:p]

hackernews = twitter.get_user_timeline(screen_name='newsycombinator', include_rts=None, count=7)
for idx, tweet in enumerate(hackernews):
    if idx == 0:
        tweet1hn = tweet['text'] + "\n"
        p = tweet1hn.find("htt")
        tweet1hn = tweet1hn[:p]
    if idx == 1:
        tweet2hn = tweet['text'] + "\n"
        p = tweet2hn.find("htt")
        tweet2hn = tweet2hn[:p]
    if idx == 2:
        tweet3hn = tweet['text'] + "\n"
        p = tweet3hn.find("htt")
        tweet3hn = tweet3hn[:p]
    if idx == 3:
        tweet4hn = tweet['text'] + "\n"
        p = tweet4hn.find("htt")
        tweet4hn = tweet4hn[:p]
    if idx == 4:
    	tweet5hn = tweet['text'] + "\n"
    	p = tweet5hn.find("htt")
    	tweet5hn = tweet5hn[:p]
    if idx == 5:
    	tweet6hn = tweet['text'] + "\n"
    	p = tweet6hn.find("htt")
    	tweet6hn = tweet6hn[:p]
    if idx == 6:
    	tweet7hn = tweet['text'] + "\n"
    	p = tweet7hn.find("htt")
    	tweet7hn = tweet7hn[:p]