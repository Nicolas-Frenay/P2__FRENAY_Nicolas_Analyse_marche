from one_book import BookScrapper
from bs4 import BeautifulSoup
import requests


class CategoryScrapper:
    """
    Object for scrapping a entire book category on https://books.toscrape.com/ . It takes the category's page's url as
    an argument.
    """

    def __init__(self, url):
        self.url = url
        # string with prefix of books' URLs
        self.links_beginning = 'https://books.toscrape.com/catalogue/'
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
        page = requests.get(url_category)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.category = soup.find('h1').text
        self.links_scrapping(soup)
        if soup.find('li', attrs={'class': 'next'}):
            next_page = soup.find('li', {'class': 'next'})
            next_link = next_page.select('li a[href]')[0]['href']
            self.url = url_category.removesuffix(self.suffix) + next_link
            self.suffix = next_link
            self.page_parsing()

    def links_scrapping(self, soup):
        """
        Methode that take a BS object as an argument, it will scrap every books link in the HTML of that one page,
    then add them in the links list
        """
        pages_to_parse = soup.select('h3 a[href]')
        for links in pages_to_parse:
            self.links_list.append(self.links_beginning + links['href'][9:])

    def data_scraping(self):
        """
        Methode that will call the book scrapper object from one_book.py, and write a CSV file with each books
    of the category
        """
        scrapper = BookScrapper()
        for books in self.links_list:
            scrapper.scrap(books)
        scrapper.write_csv(self.category + '.csv')


if __name__ == '__main__':
    category = input('Entrez l\'URL de la categorie dont vous voulez récupérer les informations : ') or (
        'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html')
    cat_scrapper = CategoryScrapper(category)
    cat_scrapper.page_parsing()
    cat_scrapper.data_scraping()
