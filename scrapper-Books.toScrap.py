from one_category import CategoryScrapper
import requests
from bs4 import BeautifulSoup

# main page of the scrapped site
site = 'https://books.toscrape.com/index.html'

# requesting url then parsing it
page = requests.get(site)
soup = BeautifulSoup(page.content, 'html.parser')

# getting links for all categories main pages
list_nav = soup.find('ul', {'class': 'nav nav-list'})
list_cat = list_nav.findAll('a')

# creating empty list to store categories urls
cat_links = []

# Inserting formated URL for each category into the cat_links list
for links in list_cat[1:]:
    cat_links.append(site.removesuffix('index.html') + links['href'])

# Looping in the list of links, for each link we call the category scrapper object from one_category.py,
# that will scrap data from all books in the category, and create a CSV file for each category
for cat in cat_links:
    scrap_cat = CategoryScrapper(cat)
    scrap_cat.page_parsing()
    scrap_cat.data_scraping()
