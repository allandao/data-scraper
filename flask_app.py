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
#app.config["DEBUG"] = True - uncomment when still testing
# static files like css files go into a subfolder called static, files like index.html go into a subfolder called templates. configure on PythonAnywhere

site_title = 'Python Web Scraping Project'
project_description = 'Paste the url of any RSS feed of any website whitelisted by PythonAnywhere to see the resulting data in an easy to read format.'
currentLink = 'onWebAppStart'

@app.route('/')
def index():
    rss_feed = get_rss(currentLink)
    return render_template('index.html', title = site_title, project_description = project_description, rss_feed = rss_feed, currentLink = currentLink)

@app.route('/', methods=['POST'])
def index_post():
    userURL = request.form['userURL']
    currentLink = userURL
    rss_feed = get_rss(userURL)
    return render_template('index.html', title = site_title, project_description = project_description, rss_feed = rss_feed, currentLink = currentLink)

@app.errorhandler(Exception)
def serverError(e):
    # can set to str(e) if outputting the error is desired
    # rss_feed does not need to be passed as index.js is set up to handle when the variable is not defined.
    # Passing in rss_feed would lead to index.js trying to process the string which would lead to non-desired output (error text)
    return render_template('index.html', title = site_title, project_description = project_description, currentLink = '')


