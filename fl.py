from flask import Flask, render_template
from get import *
import HTMLParser
import json


app = Flask(__name__)
answer = ""
data = ""

@app.route('/')
def template(randomt=randomt, answer=answer):
    arraytc = [tweet1tc, tweet2tc, tweet3tc, tweet4tc, tweet5tc, tweet6tc, tweet7tc]
    arrayph = [tweet1ph, tweet2ph, tweet3ph, tweet4ph, tweet5ph, tweet6ph, tweet7ph]
    arrayto = [tweet1to, tweet2to, tweet3to, tweet4to, tweet5to, tweet6to, tweet7to]
    arrayhn = [tweet1hn, tweet2hn, tweet3hn, tweet4hn, tweet5hn, tweet6hn, tweet7hn]
    arrays = arraytc + arrayph + arrayto + arrayhn
    randomt = random.choice(arrays)
    randomt = HTMLParser.HTMLParser().unescape(randomt)
    if randomt in arraytc:
    	answer = "techcrunch"
    if randomt in arrayph:
    	answer = "product hunt"
    if randomt in arrayto:
    	answer = "the onion"
    if randomt in arrayhn:
    	answer = "hacker news"
    data = answer
    return render_template('index.html', randomt=randomt, answer=answer, data=json.dumps(data))