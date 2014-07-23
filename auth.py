from config import APP_KEY, APP_SECRET
from twython import Twython, TwythonError

import webbrowser

# 1 step
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()


# 2 step
url = auth['auth_url']
print url
webbrowser.open(url)
print "Inserisci il pin: "
oauth_verifier = raw_input()


# 3 step
OAUTH_TOKEN = auth['oauth_token'] 
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)
OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
print "OAUTH_TOKEN: " + OAUTH_TOKEN
print "OAUTH_TOKEN_SECRET: " + OAUTH_TOKEN_SECRET

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

import time
import sys

start = time.time()

# conta il numero di richieste
crequestes = 0
while 1:
    try:
        # https://dev.twitter.com/docs/api/1.1/get/statuses/user_timeline
        user_timeline = twitter.get_user_timeline(screen_name='wireditalia', count=4)
        crequestes += 1
        sys.stdout.write('=')
        sys.stdout.flush()
    except TwythonError as e:
        print "\n"
        print e
        print str(crequestes) + " richieste"
        end = time.time()
        diff = round( (end - start) / 60 , 2)
        print str(diff) + " minuti"
        break
