from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask
import os
import pandas as pd
import time


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# Define url
url = 'https://redplanetscience.com/'
browser.visit(url)

html = browser.html
new_soup = bs(html, 'html.parser')


title = new_soup.find('div' , class_="content_title").text
print(title)

news_p = new_soup.find('div', class_="article_teaser_body").text
print(news_p)


# ## JPL Mars Space Images

# Define url

image_url= 'https://spaceimages-mars.com/'
browser.visit(image_url)

html = browser.html
image_soup = bs(html, 'html.parser')


image = image_soup.find("img", class_="headerimage fade-in")["src"]
featured_image_url = "https://spaceimages-mars.com/" + image
print(featured_image_url)

# ## Mars Facts

# Define url

mars_facts_url= 'https://galaxyfacts-mars.com/'


facts_tables = pd.read_html(mars_facts_url)
len(facts_tables)


# Selecting table and renaming columns

mars_facts_table=facts_tables[0]
mars_facts_table.columns = ["Description", "Mars", "Earth"]
mars_facts_table

# Save table in HTML format

mars_facts_url = "https://galaxyfacts-mars.com/"
browser.visit(mars_facts_url)
mars_data = pd.read_html(mars_facts_url)
mars_data = pd.DataFrame(mars_data[0])
mars_facts = mars_data.to_html(header = False, index = False)
print(mars_facts)


# ## Mars Hemispheres

url_hemisphere = "https://marshemispheres.com/"
browser.visit(url_hemisphere)

html_hemisphere = browser.html
soup = bs(html_hemisphere, "html.parser")

# Scrape all items that contain mars hemispheres information
hemispheres = soup.find_all("div", class_="item")

# Create empty list
hemispheres_info = []

# main url for loop
hemispheres_url = "https://marshemispheres.com/"

# Loop through the list of all hemispheres information
for content in hemispheres:
    title = content.find("h3").text
    hemispheres_img = content.find("a", class_="itemLink product-item")["href"]
    
    # Visit the link that contains image 
    browser.visit(hemispheres_url + hemispheres_img)
    
    # HTML Object
    image_html = browser.html
    hem_info = bs(image_html, "html.parser")
    
    # Create full image url
    img_url = hemispheres_url + hem_info.find("img", class_="wide-image")["src"]
    
    hemispheres_info.append({"title" : title, "img_url" : img_url})


# Display titles and images ulr 
    print("")
    print(title)
    print(img_url)
    print("-----------------------------------------")

