


from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
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

# Show image

from IPython.display import Image
Image(url= featured_image_url)


# ## Mars Facts

# Define url

mars_facts_url= 'https://galaxyfacts-mars.com/'
browser.visit(url)


facts_tables = pd.read_html(mars_facts_url)
len(facts_tables)

# Selecting table and renaming columns

mars_facts_table=facts_tables[0]
mars_facts_table.columns = ["Description", "Mars", "Earth"]
mars_facts_table

# Save table in HTML format

mars_facts_table_html= mars_facts_table.to_html('table.html')
mars_facts_table_html


# ## Mars Hemispheres

import time 
hemispheres_url = "https://marshemispheres.com/"
browser.visit(hemispheres_url)
html = browser.html
soup = bs(html, "html.parser")
mars_hemisphere = []


results = soup.find("div", class_ = "result-list" )
hemispheres = results.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://marshemispheres.com/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=bs(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})
    
print(mars_hemisphere)

# Back to the original page to grab more data
browser.back()

# Close the browser
browser.quit()

