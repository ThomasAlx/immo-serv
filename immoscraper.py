from inout import *
from selenium import webdriver
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import re
import os

# scraps data from IMMOWEB from the first page of a query for houses in Leuven

class ImmoScraper:

    def __init__(self, base_url=None, data_folder=None):
        self.base_url = base_url  # string
        self.data_folder = data_folder  # string
        self.data = None  # dictionary

    def get_web_data(self):
        # ignores "sponsored" from IMMOWEB
        # invokes the package to scrap data from IMMOWEB

        # get data
        driver = webdriver.Firefox()
        driver.get(self.base_url)
        html = driver.page_source
        data = BeautifulSoup(html,'html.parser')

        # get house data from html
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
        # returns scraped data as dictionary
        return self.data

    def store_data(self, name):
        # check if folder "data" exists, otherwise create it
        if os.path.exists("data"):
            pass
        else:
            os.mkdir("data")
        # save scraped data in data folder
        InOut.save_data(self.data_folder, self.data, name)
        print("\n\nData saved succesfully.")

    def load_data(self, name):
        # loads previously scraped and stored data from data folder
        print("\n\nLoading data.")
        self.data = InOut.load_data(self.data_folder, name)
        self.data = self.data[()] 

    def print_data(self):
        print("\n\nCleaned Data:\n\n", self.data)
        print("\n")

    def visualise_house_data(self):
        df = pd.DataFrame({'House ID'      :   [i for i in range(len(self.data))],
             'House ID'     :   [key for key in self.data.keys()],
             'House Price\n[\N{euro sign}]'  :   [self.data[key] for key in self.data.keys()]}) 
        print("\n\n##############################################################")
        print("Scraped Data from IMMOWEB:\n")
        print(tabulate(df, headers='keys', tablefmt='psql'))