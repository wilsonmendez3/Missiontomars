import os
import requests 
from bs4 import BeautifulSoup as bs 
import pandas as pd 
from splinter import Browser
from IPython.display import Image, display


def init_browser():
    # Make an Executable path
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_data = {}

    #Scrape Mars News 
    nasaURL = "https://mars.nasa.gov/news/"
    response = requests.get(nasaURL)
    newssoup = bs(response.text, 'html.parser')

    news_title = newssoup.find('div', class_='content_title').text
    news_p = newssoup.find('div', class_='rollover_description_inner').text
    
    #Scrape Featured Image 

    spaceimages = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(spaceimages)

    html = browser.html
    FIsoup = bs(html, 'html.parser')

    jplBaseURL = 'https://www.jpl.nasa.gov'
    imageURL = FIsoup.find('a', class_="button fancybox")["data-fancybox-href"]

    featuredImgURL = jplBaseURL + imageURL

    # Scrape Mars Weather
    MarsWxReport = "https://twitter.com/marswxreport?lang=en"
    browser.visit(MarsWxReport)

    #convert to HTML, make soup
    html = browser.html
    soup = bs(html, 'html.parser')

    mars_weather = soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_weather = mars_weather.split("pic")[0]

    # div_content = li_tags[0].find('div', class_='content')
    # for li_tag in li_tags:
    #     print(li_tag)
    # div_tweet = div_content.find('div', class_='js-tweet-text-container')
    
    # mars_weather = div_tweet.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
   
    # Scrape Mars Facts
    spacefax = "https://space-facts.com/mars/"

    spacetables = pd.read_html(spacefax , encoding= "utf-8")

    facts_df = spacetables[0]
    facts_df.columns = ['Metrics', '']
    facts_df = facts_df.set_index(['Metrics'])

    facts_table = facts_df.to_html().replace('\n', '')

    # Scrape Mars Hemispheres
    hemiURL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response = requests.get(hemiURL)
    hemiSoup = bs(response.text, "lxml")

    links = []
    hemisphere_img_urls = []
    astroBaseURL = "https://astrogeology.usgs.gov"

    div_items = hemiSoup.findAll("div", class_="item")

    for div in div_items: 
        hemisphere = {}
        div_content = div.find("div", class_="description")
        
        title = div_content.find("h3").text
        hemisphere["title"] = title
        
        href = div.find("a", class_="itemLink product-item")["href"]
        links.append(astroBaseURL + href)
        
        for link in links:
            response = requests.get(link)
            linksoup = bs(response.text, 'lxml')
               
            img_src = linksoup.find("img", {"class":"wide-image"})['src']
            img_url = astroBaseURL + img_src
            hemisphere['img_url'] = img_url
            
        hemisphere_img_urls.append(hemisphere)

    # Store the scraped data in a dictionary
    mars_data = {
        "news_title": news_title,
        "paragraph_text": news_p,
        "featured_img_url": featuredImgURL,
        "mars_weather": mars_weather,
        "mars_facts": facts_table,
        "hemisphere_img_urls": hemisphere_img_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data



