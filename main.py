from immoscraper import *
from newservice import *
from user import User
import numpy
import random

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

scrap = False

###########################################
# Scrap data from IMMOWEB
###########################################

# search for houses to buy in Leuven

scrp = ImmoScraper(base_url=url)

if (scrap):  # allows to load stored data

    scrp.get_web_data()  # ignores houses from ads "sponsored"

    scrp.store_data(data_folder)

scrp.load_data(data_folder)

scrp.print_data()

avail_house_data = scrp.get_data_dict()
house_keys = list(avail_house_data.keys())

del scrp

###########################################
# run new service
###########################################

nS = NewService(avail_house_data)

###########################################
# Simulate user interface
###########################################

exit_flag = False
curr_user_id = 0

while (exit_flag==False):

    # register new user in new service
    input_house_id = int(input("\nPlease input property id (0 to %d):\t" % (len(avail_house_data)-1)))

    curr_user = User(id=curr_user_id, house_id_interest=house_keys[input_house_id])
    nS.add_user(curr_user)
    del curr_user

    # loop for user to get proposals for different loan durations
    exit_choice_flag = False
    while(exit_choice_flag==False):

        # invoke proposal calculation and visualization
        answer = nS.prompt_choice(curr_user_id)

        # ask for new choice or exit 
        if (answer):
            exit_choice_flag = True
        else:
            exit_choice_answer = int(input("\nPress 0 to continue, 1 to exit choice:\t"))
            if (exit_choice_answer):
                exit_choice_flag = True

    # ask for new user or exit
    new_user_q = int(input("\nPress 1 for new user, or 0 to exit:\t"))
    if (new_user_q):
        curr_user_id += 1
    else:
        exit_flag = True

# -------------------------------------------------

nS.visualise()

print("\n\n--------------------------------------------------")
print("\nTERMINATION\n")
print("--------------------------------------------------\n\n")
