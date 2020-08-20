# scraper.py
# Referencing Matthew Wimberly's tutorial, found here https://codeburst.io/building-an-rss-feed-scraper-with-python-73715ca06e1f
# This was my first project related to web scraping.

import requests
from bs4 import BeautifulSoup

# scraping function
def get_rss():
    try:

        # since we are on the PythonAnyhwere platform, there are certain whitelisted websites that we must use under the free plan
        # the following link provides more details: https://www.pythonanywhere.com/whitelist/
        # not using a whitelisted link gives the following error in the server.log files https://www.pythonanywhere.com/forums/topic/12714/ and does not allow the web app to load
        r = requests.get('https://www.nlm.nih.gov/rss/auto/NLMGeneralAnnouncements.rss') # rss feeds result in xml data
        ycombinator_rssfeed = BeautifulSoup(r.content, features='xml')
        # if scraping HTML, we would set features to 'html'
        # ycombinator_rssfeed = BeautifulSoup(r.content, "lxml") - needs to have lxml installed (this is an alternative)
        print(ycombinator_rssfeed)

        article_list = []

        # add all articles to an array
        articles = ycombinator_rssfeed.findAll('item')
        for i in articles: # i being each item in the list of outputted articles from the rss feed
            title = i.find('title').text
            link = i.find('link').text
            published = i.find('pubDate').text
            article = {
                'title': title,
                'link': link,
                'published': published
                }
            article_list.append(article)
        return article_list

        # return print('scraping succeeded: ', r.status_code) # should print 200 for r.status_code
    except Exception as e:
        print('scraping failed. Here is the exception: ')
        return print(e)