from flask import Flask, render_template
from get import *
import HTMLParser
import json


app = Flask(__name__)
answer = ""
data = ""

@app.route('/')
def template(randomt=randomt, answer=answer):
    arrays = arraytc + arrayph + arrayto + arrayhn
    arraysurl = arrayurltc + arrayurlph + arrayurlto + arrayurlhn
    randomt = random.choice(arrays)
    index = arrays.index(randomt)
    url = arraysurl[index]
    randomt = HTMLParser.HTMLParser().unescape(randomt)
    url = '"' + url + '"'
    url = HTMLParser.HTMLParser().unescape(url)
    if randomt in arraytc:
    	answer = "techcrunch"
    if randomt in arrayph:
    	answer = "product hunt"
    if randomt in arrayto:
    	answer = "the onion"
    if randomt in arrayhn:
    	answer = "hacker news"
    data = answer
    return render_template('index.html', randomt=randomt, answer=answer, data=json.dumps(data), url=url)
