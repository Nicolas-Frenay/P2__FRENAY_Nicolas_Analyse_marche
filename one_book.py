from bs4 import BeautifulSoup
import requests
import csv

# Creating the columns headers row
rows = [['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax',
         'number_available', 'product_description', 'category', 'review_rating', 'image_url'], ]


# Scrapping function
def scrapping():
    global rows
    # specify url
    product_page = input("Entrez l'url du livre dont vous voulez récupérer les données :") or (
                   'https://books.toscrape.com/catalogue/it_330/index.html')

    # test web page and parse URL with BS4
    page = requests.get(product_page)
    soup = BeautifulSoup(page.content, 'html.parser')

    # create empty list to store our data
    temp_row = []

    # get some data from table inside the HTML page
    table = soup.find('table', class_='table table-striped')
    data = table.findAll('td')

    # function to get the page URL
    temp_row.append(product_page)

    # function to get UPC code from the table
    upc = data[0].text
    temp_row.append(upc)

    # function to get the book title
    temp_row.append(soup.h1.text)

    # function to get the price with tax from the table
    price_with_tax = data[2].text
    temp_row.append(price_with_tax)

    # function to get the price without tax from the table
    price_without_tax = data[3].text
    temp_row.append(price_without_tax)

    # function to get the book's availabilty from the table
    dispo = data[5].text
    temp_row.append(dispo)

    # function to get the book's description
    text_extract = soup.find('article', {'class': 'product_page'})
    desc = text_extract.findAll('p')
    description = desc[3].text
    temp_row.append(description)

    # function to get the book category
    cat = soup.find('ul', {'class': 'breadcrumb'})
    crumb_list = cat.findAll('li')
    category = crumb_list[2].text
    temp_row.append(category)

    # function to get the rating of the book
    rating_value = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
    book_rating = soup.find('div', {'class': 'col-sm-6 product_main'})
    class_list = book_rating.findAll('p')
    rating = class_list[2].attrs['class'][1]
    for rate in rating_value:
        if rate == rating:
            final_rating = (str(rating_value.index(rate)) + '/5')
            temp_row.append(final_rating)

    # function to get the book image's URL
    source = soup.find('div', {'class': 'item active'})
    link = source.find('img')
    img_link = 'https://books.toscrape.com'
    img_link = img_link + link['src'][5:]
    temp_row.append(img_link)

    # insertion temp row
    rows.append(temp_row)

    # writing data in csv file
    with open("one_book_scrap.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


if __name__ == '__main__':
    scrapping()
