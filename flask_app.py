# Flask with Python 3.7
# Started on August 19, 2020 as a way to practice Python and to learn about Flask
# http://allandao.pythonanywhere.com/

# Resources
# https://blog.pythonanywhere.com/121/
# https://www.techiediaries.com/flask-tutorial-templates/
# flask render_template example

# PEP-8 (Style Guide) Recommendation - one line per module or from ___ import statement
from flask import Flask
from flask import request
from flask import render_template
from scraper import get_rss

app = Flask(__name__)
app.config["DEBUG"] = True # remove when finished testing
# static files like css files go into a subfolder called static, files like index.html go into a subfolder called templates. configure on PythonAnywhere

@app.route('/')
def index():
    header_page = "Python Web Scraping Project"
    rss_feed = get_rss()
    return render_template('index.html', title = header_page, paragraph = "Paste a url of any RSS feed of any website whitelisted by PythonAnywhere to see the resulting data in a easy to read format.", rss_feed = rss_feed)

@app.route('/', methods=['POST'])
def index_post():
    #pasted_url = get_rss()
    pasted_url = request.form['url']
    return pasted_url
    #return render_template('index.html', title = "Simple Python Web Scraper", paragraph = "Paste a url of any RSS feed to see the resulting data in a easy to read format", url = pasted_url)