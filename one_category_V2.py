from one_book_V2 import BookScrapper
from urllib.request import urlopen
import re


class CategoryScrapper:
    """
    Object for scrapping a entire book category on http://books.toscrape.com/ . It takes the category's page's url as
    an argument.
    """

    def __init__(self, url):
        if re.search('^https', url):
            self.url = 'http' + url.removeprefix('https')
        else:
            self.url = url
        # string with prefix of books' URLs
        self.links_beginning = 'http://books.toscrape.com/catalogue/'
        # list storing books links
        self.links_list = []
        self.category = ''
        self.suffix = 'index.html'

    def page_parsing(self):
        """
        Methode for parsing the category page, then send BS object to links scrapping function. If there is a "next"
    button on the page, it will call itself again with the next page's URL.
        """
        url_category = self.url
        html_page = urlopen(url_category)
        html_data = html_page.read().decode('utf-8')
        self.category = re.search('(?<=<h1>).*?(?=</h1)', html_data).group()
        self.links_scrapping()
        if re.search('(?<=class="next").*?(?=</a>)', html_data):
            next_button = re.search('(?<=class="next").*?(?=</a>)', html_data).group()
            next_link = re.search('(?<=href=").*?(?=">)', next_button).group()
            self.url = url_category.removesuffix(self.suffix) + next_link
            self.suffix = next_link
            self.page_parsing()

    def links_scrapping(self):
        """
        Methode that will scrap every books link in the HTML of that one page,
    then add them in the links list
        """
        html_page = urlopen(self.url)
        html_data = html_page.read().decode('utf-8')
        list_books_link = re.findall('(?<=<h3>).*?(?=</h3>)', html_data)
        for books in list_books_link:
            book_link = re.search('(?<=href=").*?(?=" )', books).group()
            self.links_list.append(self.links_beginning + book_link[9:])

    def data_scraping(self):
        #     """
        #     Methode that will call the book scrapper object from one_book.py, and write a CSV file with each books
        # of the category
        #     """
        scrapper = BookScrapper()
        for books in self.links_list:
            scrapper.scrap(books)
        scrapper.write_csv(self.category + '.csv')


if __name__ == '__main__':
    category = input('Entrez l\'URL de la categorie dont vous voulez récupérer les informations : ') or (
        'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html')
    cat_scrapper = CategoryScrapper(category)
    cat_scrapper.page_parsing()
    cat_scrapper.data_scraping()
