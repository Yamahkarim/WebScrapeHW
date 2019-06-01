#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup 
import requests
import pandas as pd


# # Nasa Mars Website

# In[3]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)


# In[4]:


#visit Nasa's Mars Webpage 
url = 'https://mars.nasa.gov/news/'
browser.visit(url) 


# In[5]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[6]:


recent = soup.find('div', class_='list_text').text
news_title = recent.find_all('div', class_='content_title').text
news_pgraph = recent.find_all('div', class_='article_teaser_body').text

print(news_title)
print(news_pgraph)


# # JPL Mars Space Images 

# In[7]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
#create soup object
soup = BeautifulSoup(html, 'html.parser')


# In[8]:


# Scrape URL for featured Mars image
img_find = soup.find('footer')
img = img_find.find('a', class_='button fancybox')['data-fancybox-href']
img_url = "https://jpl.nasa.gov" + img
featured_image_url = img_url
print(featured_image_url)


# # Mars Weather
# 

# In[9]:


# Retrieve most recent tweet about the weather on Mars
url = 'https://twitter.com/marswxreport?lang=en'
response = requests.get(url)
browser.visit(url)


# In[10]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[11]:


tweet_box = soup.find('div', class_='js-tweet-text-container')
tweet = tweet_box.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
mars_weather = tweet
print(mars_weather)


# # Mars Facts

# In[12]:


url = 'https://space-facts.com/mars/'
response = requests.get(url)
browser.visit(url)


# In[13]:


Mars_df = pd.read_html('https://space-facts.com/mars/')[0]
Mars_df.columns=['description', 'value']
Mars_df.set_index('description', inplace=True)
Mars_df


# In[15]:


#read the data to HTML
Mars_df.to_html()


# In[17]:


browser.quit()


# # Mars Hemisphere Images

# In[17]:


#Visit Website for Mars Hemisphere Images 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[18]:


hemisphere_image_urls = []

for h in range(4):
    browser.find_by_tag('h3')[h].click()   
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h2', class_='title').text
    img_url_partial = soup.find('img', class_='wide-image')['src']
    img_url = 'https://astrogeology.usgs.gov' + img_url_partial
    dict = {'title':title, 'img_url':img_url}
    hemisphere_image_urls.append(dict)
    browser.back()


# In[19]:


hemisphere_image_urls


# In[ ]:




