from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser
import numpy as np
import time

def scrape():
    ###NASA MARS NEWS
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    title = soup.find(class_='content_title')
    paragraph = soup.find(class_='rollover_description_inner')

    title = title.find('a').text
    paragraph = paragraph.text

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find_all('a', class_='fancybox')

    featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23205_hires.jpg'

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    weather = soup.find('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    mars_weather = str(weather).split('InSight ')[1].replace('\n','').split('<a')[0]

    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    facts = soup.find('tbody')

    facts_dic = str(facts).replace('\n','').split('<strong>')

    facts_dic.pop(0)

    key = []
    value = []
    for d in facts_dic:
        text = d.split(':')
        k = text[0]
        v = text[1].split('mn-2">')[1].split('<')[0]
        key.append(k)
        value.append(v)
        
    mars_facts = dict(zip(key, value))

    mars_facts

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    #html = browser.html
    #soup = BeautifulSoup(html, 'html.parser')

    links_k = ['Cerberus Hemisphere Enhanced','Schiaparelli Hemisphere Enhanced',
            'Syrtis Major Hemisphere Enhanced','Valles Marineris Hemisphere Enhanced']
    links_v = []
    for x in links_k:
        browser.click_link_by_partial_text(x)
        time.sleep(5)
        html = browser.html
        soup = BeautifulSoup(html, 'lxml')
        url_links = soup.find('div',class_='downloads')
        l = str(url_links.find('a')).split('"')[1]
        browser.back()
        links_v.append(l)

    links_dict = dict(zip(links_k,links_v))

    hemisphere_image_urls = links_dict

    mars_weather

    news_title = title
    news_p = paragraph

    x = {'news_title':news_title}
    y = {'news_p':news_p}
    z = {'featured_image_url':featured_image_url}
    q = {'mars_weather':mars_weather}

    all_data = {**x,**y,**z,**q,**mars_facts,**hemisphere_image_urls}

    return all_data