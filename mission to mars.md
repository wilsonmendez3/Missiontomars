

```python
import os
import requests 
from bs4 import BeautifulSoup as bs 
import pandas as pd 
from splinter import Browser
from IPython.display import Image, display
```


```python
# Make an Executable path
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
```

# NASA Mars News


```python
#Visit Nasa
nasaURL = "https://mars.nasa.gov/news/"
browser.visit(nasaURL)

#convert to HTML, make soup
html = browser.html
soup = bs(html, 'html.parser')

news_title = soup.find('div', class_='content_title').text
print(f'Latest NASA news article: {news_title}')
news_p = soup.find('div', class_='article_teaser_body').text
print(news_p)
```

    Latest NASA news article: NASA's Curiosity Mars Rover Finds a Clay Cache
    The rover recently drilled two samples, and both showed the highest levels of clay ever found during the mission.


# Featured NASA Space Image 


```python
#Retrieve featured Space Image
spaceimages = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(spaceimages)

#convert to HTML, make soup
html = browser.html
soup = bs(html, 'html.parser')

#get featured image URL & its Description
imageURL = soup.find('a', class_="button fancybox")["data-fancybox-href"]
imageDPN = soup.find('a', class_="button fancybox")["data-description"]
#print(imageURL)

baseURL = "https://www.jpl.nasa.gov"
spaceimageURL = baseURL + imageURL

display(Image(url=spaceimageURL, width=400))
print(f'Featured NASA Image: {spaceimageURL}')
print(imageDPN)
```


<img src="https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA12831_ip.jpg" width="400"/>


    Featured NASA Image: https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA12831_ip.jpg
    This infrared image taken by NASA's Wide-field Infrared Survey Explorer shows a star-forming cloud teeming with gas, dust and massive newborn stars.


# Mars Weather via @MarsWxReport


```python
MarsWxReport = "https://twitter.com/marswxreport?lang=en"
browser.visit(MarsWxReport)

#convert to HTML, make soup
html = browser.html
soup = bs(html, 'html.parser')

mars_weather = soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").getText()[0:166]
print(f'Latest tweet from @MarsWxReport: {mars_weather}')

mars_img = soup.find("div", class_="AdaptiveMedia-photoContainer js-adaptive-photo ")["data-image-url"]
print(mars_img)
display(Image(url=mars_img, width=400))
```

    Latest tweet from @MarsWxReport: InSight sol 181 (2019-05-31) low -100.6ºC (-149.1ºF) high -20.7ºC (-5.3ºF)
    winds from the SW at 5.1 m/s (11.3 mph) gusting to 14.9 m/s (33.3 mph)
    pressure at 7.50 hPa
    https://pbs.twimg.com/media/D7805YvX4AA1M6s.jpg



<img src="https://pbs.twimg.com/media/D7805YvX4AA1M6s.jpg" width="400"/>


# Space Facts


```python
spacefax = "https://space-facts.com/mars/"

spacetables = pd.read_html(spacefax , encoding= "utf-8")
spacetables
```




    [                      0                              1
     0  Equatorial Diameter:                       6,792 km
     1       Polar Diameter:                       6,752 km
     2                 Mass:  6.42 x 10^23 kg (10.7% Earth)
     3                Moons:            2 (Phobos & Deimos)
     4       Orbit Distance:       227,943,824 km (1.52 AU)
     5         Orbit Period:           687 days (1.9 years)
     6  Surface Temperature:                  -153 to 20 °C
     7         First Record:              2nd millennium BC
     8          Recorded By:           Egyptian astronomers]




```python
df = spacetables[0]
df.columns = ['Metrics', '']
df = df.set_index(['Metrics'])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th>Metrics</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Equatorial Diameter:</th>
      <td>6,792 km</td>
    </tr>
    <tr>
      <th>Polar Diameter:</th>
      <td>6,752 km</td>
    </tr>
    <tr>
      <th>Mass:</th>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>Moons:</th>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>Orbit Distance:</th>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
      <th>Orbit Period:</th>
      <td>687 days (1.9 years)</td>
    </tr>
    <tr>
      <th>Surface Temperature:</th>
      <td>-153 to 20 °C</td>
    </tr>
    <tr>
      <th>First Record:</th>
      <td>2nd millennium BC</td>
    </tr>
    <tr>
      <th>Recorded By:</th>
      <td>Egyptian astronomers</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_html().replace('\n', '')
```




    '<table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th></th>      <th></th>    </tr>    <tr>      <th>Metrics</th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Equatorial Diameter:</th>      <td>6,792 km</td>    </tr>    <tr>      <th>Polar Diameter:</th>      <td>6,752 km</td>    </tr>    <tr>      <th>Mass:</th>      <td>6.42 x 10^23 kg (10.7% Earth)</td>    </tr>    <tr>      <th>Moons:</th>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>Orbit Distance:</th>      <td>227,943,824 km (1.52 AU)</td>    </tr>    <tr>      <th>Orbit Period:</th>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>Surface Temperature:</th>      <td>-153 to 20 °C</td>    </tr>    <tr>      <th>First Record:</th>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>Recorded By:</th>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'



# Hemispheres of Mars


```python
hemiURL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemiURL)

baseURL = "https://astrogeology.usgs.gov"


html = browser.html
soup = bs(html, "html.parser")
links = []
hemisphere_img_urls = []

# img_url = 

div_result = soup.find("div", class_="collapsible results")
div_items = div_result.findAll("div", class_="item")

for div in div_items: 
    hemisphere = {}
    div_content = div.find("div", class_="description")
    
    title = div_content.find("h3").text
    hemisphere["title"] = title
    
    href = div.find("a", class_="itemLink product-item")["href"]
    links.append(baseURL + href)
    
    for link in links:
        response = requests.get(link)
        soup = bs(response.text, 'lxml')
        
        
        img_src = soup.find("img", {"class":"wide-image"})['src']
        img_url = baseURL + img_src
        hemisphere['img_url'] = img_url
        
    hemisphere_img_urls.append(hemisphere)

for item in hemisphere_img_urls:
    print(item)
    display(Image(url=img_url, width=400))

#print(links)
```

    {'title': 'Cerberus Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'}



<img src="https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg" width="400"/>


    {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'}



<img src="https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg" width="400"/>


    {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'}



<img src="https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg" width="400"/>


    {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}



<img src="https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg" width="400"/>

