from one_category_V2 import CategoryScrapper
from urllib.request import urlopen
import re

# getting main page of the scrapped site
site = 'http://books.toscrape.com/index.html'
html_page = urlopen(site)
html_data = html_page.read().decode('utf-8')

# creating empty list to store categories urls
cat_links = []

#getting links for all categories, then storing them in a list
menu_lists = re.search('(?<=<ul>).*?(?=</ul>)', html_data, re.DOTALL).group()
li_list = re.findall('(?<= <li>).*?(?=</li>)', menu_lists, re.DOTALL)
for items in li_list:
    link = re.search('(?<=href=").*?(?=">)', items).group()
    cat_links.append(site.removesuffix('index.html') + link)

# Looping in the list of links, for each link we call the category scrapper object from one_category.py,
# that will scrap data from all books in the category, and create a CSV file for each category
for cat in cat_links:
    scrap_cat = CategoryScrapper(cat)
    scrap_cat.page_parsing()
    scrap_cat.data_scraping()
