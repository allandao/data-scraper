# scraper.py

# Referencing Matthew Wimberly's tutorial, found here https://codeburst.io/building-an-rss-feed-scraper-with-python-73715ca06e1f
# This was my first project related to web scraping.
# Using the article above as a preliminary to build a web scraper, I extended this
# into a project with the goal of creating a web app hosted on PythonAnywhere.
# Includes comments documenting the learning process, including errors, resources used, and different solutions attempted.

import requests
from bs4 import BeautifulSoup

# scraping function
def get_rss(rss_feed_url):
    try:
        if rss_feed_url == 'onWebAppStart':
            return 'onWebAppStart'
        else:
            # since we are on the PythonAnyhwere platform, there are certain whitelisted websites that we must use under the free plan
            # the following link provides more details: https://www.pythonanywhere.com/whitelist/
            # not using a whitelisted link gives the following error in the server.log files: https://www.pythonanywhere.com/forums/topic/12714/ and does not allow the web app to load
            r = requests.get(rss_feed_url) # GET HTTP method used to obtain xml data
            rssfeed_data = BeautifulSoup(r.content, features='xml')
            # if scraping HTML, we would set features to 'html'
            # rssfeed_data = BeautifulSoup(r.content, "lxml") - needs to have lxml installed (this is an alternative)

            # debug
            # print(rssfeed_data)

            article_list = []

            # add all articles to an array
            articles = rssfeed_data.findAll('item')
            for i in articles: # i being each item in the list of outputted articles from the rss feed
                title = i.find('title').text
                link = i.find('link').text
                publishingDate = i.find('pubDate').text
                article = {
                    'title': title,
                    'link': link,
                    'publishingDate': publishingDate
                    }
                article_list.append(article)

            # solution using jinja2 to render the desired output is preferred to the attempted solution below as line breaks are correctly implemented
            # article_list_formatted = []
            # for x in range(len(article_list)):
                # article_list_formatted.append(article_list[x]['title'] + ' - ' + article_list[x]['publishingDate'] + ' \nLink: ' + article_list[x]['link'])

            # debug
            # return print('scraping succeeded: ', r.status_code) # should print 200 for r.status_code
            return article_list

    except Exception as e:
        # debug
        # print('Scraping failed. Here is the exception: ')
        print(e)

        # no return None statement (never return null as described in Clean Code) and since desired outputted data is nothing






