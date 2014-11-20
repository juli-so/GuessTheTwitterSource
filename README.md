Guess The Twitter Source
======

The Idea
-------
3 hour project that I put together after @semil tweeted "Fun app idea: Display real tech headline pulled from Twitter & hide   source. User guesses: Hacker News, The Onion, TechCrunch, Product Hunt?" (https://twitter.com/semil/status/491451396424990721)
 
**Live Version:** http://guessthetwittersource.heroku.com
 
How it works
-------
Pulls recent tweets from 4 different Twitter feeds (@newsycombinator, @theonion, @techcrunch, @ProductHunt), eliminates links, and randomly selects one tweet from the accounts.
 
Technicalities
-------
Built on Flask, Python, JavaScript (uses localStorage to store current streak).
 
Build it
-------
To run locally, create a config.py file with your keys:
(APP_KEY = "", APP_SECRET = "", OAUTH_TOKEN = "", OAUTH_TOKEN_SECRET = "") and then run your "fl.py" file
 
Improvements Coming
 -------
- Cleaner Code
- Select Twitter Accounts on User End
