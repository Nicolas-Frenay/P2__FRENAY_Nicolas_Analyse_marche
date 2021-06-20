from bs4 import BeautifulSoup
import requests
import csv
from os import mkdir


class BookScrapper:
    """
    Book scrapper object, it will grab all infos on the book page which url's is give as a argument
    """

    def __init__(self):
        # Creating the columns headers row
        self.rows = [['product_page_url', 'universal_product_code', 'title', 'price_including_tax',
                      'price_excluding_tax', 'number_available', 'product_description', 'category',
                      'review_rating', 'image_url'], ]
        self.title = ''
        self.category = ''
        self.img_link = ''
        try:
            mkdir('csv_files')
        except FileExistsError:
            pass
        try:
            mkdir('images')
        except FileExistsError:
            pass

    def scrap(self, url):
        """
        Methode that will scrap the book infos from its https://books.toscrape.com/ page. It will scrap the product
        page url, the UPC, the title, the price (both with and without tax), the number available, the description,
        the category, the rating and the image url.
        """
        # test web page and parse URL with BS4
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # create empty list to store our data
        temp_row = []

        # get some data from table inside the HTML page
        table = soup.find('table', class_='table table-striped')
        data = table.findAll('td')

        # get the page URL
        temp_row.append(url)

        # get UPC code from the table
        upc = data[0].text
        temp_row.append(upc)

        # to get the book title
        self.title = soup.h1.text
        temp_row.append(self.title)

        # get the price with tax from the table
        price_with_tax = data[2].text
        temp_row.append(price_with_tax)

        # get the price without tax from the table
        price_without_tax = data[3].text
        temp_row.append(price_without_tax)

        # get the book's availabilty from the table
        dispo = data[5].text
        temp_row.append(dispo)

        # get the book's description
        text_extract = soup.find('article', {'class': 'product_page'})
        desc = text_extract.findAll('p')
        description = desc[3].text
        temp_row.append(description)

        # get the book category
        cat = soup.find('ul', {'class': 'breadcrumb'})
        crumb_list = cat.findAll('li')
        category = crumb_list[2].text
        self.category = category.strip()
        temp_row.append(category)

        # get the rating of the book
        rating_value = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five']
        book_rating = soup.find('div', {'class': 'col-sm-6 product_main'})
        class_list = book_rating.findAll('p')
        rating = class_list[2].attrs['class'][1]
        for rate in rating_value:
            if rate == rating:
                final_rating = (str(rating_value.index(rate)) + '/5')
                temp_row.append(final_rating)
                break

        # get the book image's URL
        source = soup.find('div', {'class': 'item active'})
        link = source.find('img')
        img_link = 'https://books.toscrape.com'
        img_link = img_link + link['src'][5:]
        self.img_link = img_link
        temp_row.append(img_link)

        # insertion temp row
        self.rows.append(temp_row)

        #Downloading image and recording it in images/category folder
        try:
            mkdir('images/' + self.category)
        except FileExistsError:
            pass
        image = requests.get(self.img_link)
        img_file = open('images/' + self.category + '/' + self.title.replace('/', ' - ') + '.jpg', 'wb')
        img_file.write(image.content)
        img_file.close()

    #writing data in csv file
    def write_csv(self, csv_name=None):
        """
        Methode that will write the infos of the book in a CSV file, with proper column headers. Default name will be
        the book title, but you can pass any name for the file in argument.
        """
        csv_file = csv_name or (self.title + '.csv')
        row_list = self.rows
        with open('csv_files/' + csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)


if __name__ == '__main__':
    # specify url
    product_page = input("Entrez l'url du livre dont vous voulez récupérer les données :") or (
        'https://books.toscrape.com/catalogue/it_330/index.html')
    scrapper = BookScrapper()
    scrapper.scrap(product_page)
    scrapper.write_csv()
