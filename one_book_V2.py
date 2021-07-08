from urllib.request import urlopen
import re


rows = [['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
                  'price_excluding_tax', 'number_available', 'product_description', 'category',
                  'review_rating', 'image_url'], ]
    # self.title = ''
    # self.category = ''
    # self.img_link = ''
    # try:
    #     mkdir('csv_files')
    # except FileExistsError:
    #     pass
    # try:
    #     mkdir('images')
    # except FileExistsError:
    #     pass

temp_row = []
url = 'http://books.toscrape.com/catalogue/it_330/index.html'
html_page = urlopen(url)
html_data = html_page.read().decode('utf-8')

#URL
temp_row.append(url)

# #UPC
book_UPC = re.search('(?<=<th>UPC</th><td>).*?(?=</td>)', html_data).group()
temp_row.append(book_UPC)
#
# #title
book_title = re.search('(?<=<h1>).*?(?=</h1>)',html_data).group()
temp_row.append(book_title)

#price inc
book_price_TTC = re.search('(?<=<th>Price \(incl\. tax\)</th><td>).*?(?=</td>)', html_data).group()
temp_row.append(book_price_TTC)
#
# #price exc
price_HT = re.search('(?<=<th>Price \(excl\. tax\)</th><td>).*?(?=</td>)', html_data).group()
temp_row.append(price_HT)

#avail
availability = re.search('(?<=</i>).*?(?=</p>)', html_data, re.DOTALL).group()
availability = availability.strip()
temp_row.append(availability)


#description
desc_select = re.search('(?<=Product Description</h2>).*?(?=<div)', html_data, re.DOTALL).group()
description = re.search('(?<=<p>).*?(?=</p>)', desc_select, re.DOTALL).group()
temp_row.append(description)

#category
cat_selec = re.search('(?<=/category/books/).*?(?=</li>)', html_data, re.DOTALL).group()
category = re.search('(?<=">).*?(?=</a>)', cat_selec).group()
temp_row.append(category)

#review
rating_value = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five')
rating = re.search('(?<=star-rating ).*?(?=">)',html_data).group()
for rate in rating_value:
    if rate == rating:
        final_rating = (str(rating_value.index(rate)) + '/5')
        temp_row.append(final_rating)
        break


#img url
img_url = re.search('(?<=img src=).*?(?=" alt=")',html_data).group()
img_link = 'https://books.toscrape.com'
img_link = img_link + img_url[5:]
temp_row.append(img_link)


print(temp_row)


