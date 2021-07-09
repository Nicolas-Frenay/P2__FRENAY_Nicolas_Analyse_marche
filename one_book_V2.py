from urllib.request import urlopen
from os import mkdir
import re
import csv


class BookScrapper:
    """
    Book scrapper object, it will grab all infos on the book page which url's is give as an argument for its scrap
    methode
    """

    def __init__(self):
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

    def scrap(self, book_url):
        """
        Method that scrap data for one book which url's had been given in argmuent, and store those infos in a list,
        add this list to the final list that will be written in a csv file, and download the image of the book, and
        store it in a folder named after the category of the book.
        """
        temp_row = []
        if re.search('^https', book_url):
            url = 'http' + book_url.removeprefix('https')
        else:
            url = book_url

        html_page = urlopen(url)
        html_data = html_page.read().decode('utf-8')

        # URL
        temp_row.append(url)

        # UPC
        book_UPC = re.search('(?<=<th>UPC</th><td>).*?(?=</td>)', html_data).group()
        temp_row.append(book_UPC)

        # title
        book_title = re.search('(?<=<h1>).*?(?=</h1>)', html_data).group()
        self.title = book_title
        temp_row.append(book_title)

        # price inc
        book_price_TTC = re.search('(?<=<th>Price \(incl\. tax\)</th><td>).*?(?=</td>)', html_data).group()
        temp_row.append(book_price_TTC)

        # price exc
        price_HT = re.search('(?<=<th>Price \(excl\. tax\)</th><td>).*?(?=</td>)', html_data).group()
        temp_row.append(price_HT)

        # avail
        availability = re.search('(?<=</i>).*?(?=</p>)', html_data, re.DOTALL).group()
        availability = availability.strip()
        temp_row.append(availability)

        # description
        if re.search('(?<=Product Description</h2>).*?(?=<div)', html_data, re.DOTALL):
            desc_select = re.search('(?<=Product Description</h2>).*?(?=<div)', html_data, re.DOTALL).group()
            description = re.search('(?<=<p>).*?(?=</p>)', desc_select, re.DOTALL).group()
            temp_row.append(description)
        else:
            temp_row.append('Aucune déscription disponible')

        # category
        cat_selec = re.search('(?<=/category/books/).*?(?=</li>)', html_data, re.DOTALL).group()
        category = re.search('(?<=">).*?(?=</a>)', cat_selec).group()
        self.category = category
        temp_row.append(category)

        # review
        rating_value = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five')
        rating = re.search('(?<=star-rating ).*?(?=">)', html_data).group()
        for rate in rating_value:
            if rate == rating:
                final_rating = (str(rating_value.index(rate)) + '/5')
                temp_row.append(final_rating)
                break

        # img url
        img_url = re.search('(?<=img src=).*?(?=" alt=")', html_data).group()
        img_link = 'http://books.toscrape.com'
        img_link = img_link + img_url[5:]
        self.img_link = img_link
        temp_row.append(img_link)

        # insertion temp row
        self.rows.append(temp_row)

        # Downloading image and recording it in images/category folder
        try:
            mkdir('images/' + self.category)
        except FileExistsError:
            pass
        img_file = open('images/' + self.category + '/' + self.title.replace('/', ' - ') + '.jpg', 'wb')
        img_file.write(urlopen(self.img_link).read())
        img_file.close()

    # writing data in csv file
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
        'http://books.toscrape.com/catalogue/it_330/index.html')
    scrapper = BookScrapper()
    scrapper.scrap(product_page)
    scrapper.write_csv()
