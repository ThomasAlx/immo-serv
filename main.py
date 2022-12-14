from immoscraper import *
from newservice import *
from interface import *

# uses new service

# scrap FLAG IS SET TO FALSE: SET TO TRUE IF YOU WANT TO USE THE SCRAPER 

#################################################
# Parameters
#################################################

url = "https://www.immoweb.be/en/search/house/for-sale/leuven/3000?countries=BE&page=1&orderBy=relevance"

data_folder = "data"

scrap = False  # SET THIS TRUE IF YOU WANT TO USE WEBSCRAPER

###########################################
# New service
###########################################

nS = NewService()

###########################################
# Scrap data from IMMOWEB using new service
###########################################

# NEW SERVICE FUNCTIONALITY
nS.set_web_scraper(url, data_folder)

if (scrap):  # is going to scrap data from IMMOWEB

    # NEW SERVICE FUNCTIONALITY
    nS.scrap_data("immo-cleaned-data.npy")

else:  # load the data from data local folder

    # NEW SERVICE FUNCTIONALITY
    nS.load_house_data("immo-cleaned-data.npy")

###########################################
# Simulate user interface to use new service
###########################################

exit_flag = False
curr_user_id = 0

while (exit_flag==False):

    # user input: house preference
    house_id_choice = input_house_id(nS) 

    # NEW SERVICE FUNCTIONALITY
    nS.add_user(curr_user_id, house_id_choice)

    # loop for user to get proposals for different loan durations
    exit_choice_flag = False
    curr_loan_id = 0
    while(exit_choice_flag==False):
        
        # user input: preferred loan duration
        loan_duration = int(input("\nInsert loan duration in months:\t"))

        # NEW SERVICE FUNCTIONALITY
        # invoke proposal calculation and visualization
        answer = nS.propose_loan(curr_user_id, loan_duration, curr_loan_id)

        # user input: ask for new choice or exit 
        curr_loan_id, exit_choice_flag = new_choice_question(answer, exit_choice_flag, curr_loan_id)

    # user input: ask for new user or exit
    curr_user_id, exit_flag = new_user_question(curr_user_id, exit_flag)
    

# -------------------------------------------------

###########################################
# Invoke backend service via new service 
# for visualisation
###########################################

# NEW SERVICE FUNCTIONALITY
nS.visualise_overview()

print("\n\n--------------------------------------------------")
print("\nTERMINATION\n")
print("--------------------------------------------------\n\n")


