from immoscraper import *

#################################################
# Ideas 
#################################################

# maybe use pytests to test the whole system ?

# should use newService to manage data and eventually visualize everything 

#################################################
# Parameters
#################################################

url = "https://www.immoweb.be/en/search/house/for-sale/leuven/3000?countries=BE&page=1&orderBy=relevance"

data_folder = "data"

scrap = True

###########################################

# search for houses to buy in Leuven

scrp = ImmoScraper(base_url=url)

if (scrap):

    scrp.get_web_data()  # ignores houses from ads "sponsored"

    scrp.store_data(data_folder)

scrp.load_data(data_folder)

scrp.print_data()
