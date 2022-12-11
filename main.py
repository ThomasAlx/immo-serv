from immoscraper import *
from newservice import *
from user import User
from interface import *

# uses new service

#################################################
# Parameters
#################################################

url = "https://www.immoweb.be/en/search/house/for-sale/leuven/3000?countries=BE&page=1&orderBy=relevance"

data_folder = "data"

scrap = False

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
    nS.scrap_data()

else:  # load the data from data local folder

    # NEW SERVICE FUNCTIONALITY
    nS.load_house_data()

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
    while(exit_choice_flag==False):
        
        # user input: preferred loan duration
        loan_duration = int(input("\nInsert loan duration in months:\t"))

        # NEW SERVICE FUNCTIONALITY
        # invoke proposal calculation and visualization
        answer = nS.propose_loan(curr_user_id, loan_duration)

        # user input: ask for new choice or exit 
        exit_choice_flag = new_choice_question(answer, exit_choice_flag)

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


