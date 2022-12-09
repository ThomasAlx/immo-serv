from reader import Reader
from selenium import webdriver
from bs4 import BeautifulSoup
import re

class ImmoScraper:

    def __init__(self, base_url=None):
        self.base_url = base_url
        self.data = None

    def print_data(self):
        print("\n\nCleaned Data:\n\n", self.data)
        print("\n")

    def get_web_data(self):
        # ignores "sponsored" from IMMOWEB

        driver = webdriver.Firefox()
        driver.get(self.base_url)
        html = driver.page_source
        data = BeautifulSoup(html,'html.parser')

        houses = data.find_all('article', class_="card card--result card--xl")

        self.check_succesful_scraping(houses)

        cleaned_data = {}

        for house in houses:

            # get the id of the <article>
            id_str = house.attrs["id"]

            # clean
            id_str = self.clean_id(id_str)

            # get price
            price_obj = house.find_all('span', class_="sr-only")
            price_str = price_obj[0].get_text(strip=True)

            # clean
            price_str = self.clean_price(price_str)

            # store in dictionary
            cleaned_data[id_str] = price_str

        self.data = cleaned_data  # update member variable

    def check_succesful_scraping(self, houses):
        if houses==[]:
            raise Exception("No houses found. Check if scraping was succesful.")

    def clean_price(self, str):
        # removes ranges and euro signs. Keeps largest value.
        str = str.replace("\N{euro sign}","")
        price_str = re.sub('From.*?To ', '', str, flags=re.DOTALL)
        return int(price_str)

    def clean_id(self, str):
        return str.replace("classified_","")

    def get_data_dict(self):
        return self.data

    def store_data(self,folder):
        Reader.save_data(folder, self.data)
        print("\n\nData saved succesfully.")

    def load_data(self, folder):
        print("\n\nLoading data.")
        self.data = Reader.load_data(folder)
        self.data = self.data[()] 