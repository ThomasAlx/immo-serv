from backendserv import BackEndService
from user import User
from immoscraper import ImmoScraper

import pandas as pd
from tabulate import tabulate

class NewService:

    def __init__(self, house_data=None):
        self.house_data = house_data  # dictionary of the scraped data from IMMOWEB
        self.users = []  # list of user objects
        self.web_scraper = None  # object of scraper class

    def propose_loan(self, user_id, loan_duration, loan_id):
        # main function of new service

        self.calculate_loan(loan_duration, user_id, loan_id)

        self.visualise_proposal(user_id, loan_id)

        # user input to accept calculated loan
        answer = self.get_answer()

        # depending on the answer, it sets the loan status to proposed or accepted
        self.set_loan_status(answer, user_id, loan_id)

        return answer

    def calculate_loan(self, duration, user_id, loan_id):
        # Input:
        #       - duration: duration of loan in months
        #       - user_id:  id of user in self.users list
        # Output:
        #       - proposal: loan instance 

        # extract the current user
        curr_user = self.users[user_id]

        # get the house id and price
        house_id = curr_user.house_id_interest
        house_price = self.house_data[house_id]
        
        # sets parameters of current loan of current user
        curr_user.set_loan(house_id, house_price, duration, loan_id) 

        # calculate loan specifics
        curr_user.calc_loan(loan_id)

    def get_answer(self):
        # user can reject or accept proposed loan

        check_flag = True
        while (check_flag):
            answer = input("\nTo accept proposal press: 'y' / To cancel press: 'n'\t")
            check_flag = False
            if (answer!='n' and answer!='y'):
                print("\nPlease enter a valid option.")
                check_flag = True
        return answer

    def visualise_proposal(self, user_id, loan_id):
        # visualises the proposal in a small table for the interface

        proposal = self.users[user_id].loans[loan_id]
        df = pd.DataFrame({'User ID'      :   [self.users[user_id].id],
             'House ID'     :   [proposal.house_id],
             'House Price\n[\N{euro sign}]'  :   [proposal.house_price],
             'Loan Duration\n[months]':   [proposal.loan_duration],
             'Rate'         :   [proposal.rate],
             'Final Price\n[\N{euro sign}]'  :   [proposal.total_amount],
             'Montlhy Pay\n[\N{euro sign}]'  :   [proposal.monthly_inst]}) 
        print("\n\n##############################################################")
        print("New Proposal:\n")
        print(tabulate(df, headers='keys', tablefmt='psql'))
        
    def set_loan_status(self, answer, user_id, loan_id):
        # changes the status of the loan from "proposed" to "accepted"
        if (answer=='y'):
            self.users[user_id].loans[loan_id].status = "accepted"

#-------------------------------------

    def add_user(self, curr_user_id, input_house_id):
        # adds a user to the users list

        keys = list(self.house_data.keys())
        new_user = User(id=curr_user_id, house_id_interest=keys[input_house_id])
        self.users.append(new_user)

#-------------------------------------

    def visualise_overview(self):
        # invokes backend service
        BackEndService.visualise(self)

#-------------------------------------

    def set_web_scraper(self, url, folder):
        self.web_scraper = ImmoScraper(base_url=url, data_folder=folder)

    def load_house_data(self, name):
        # Loads data from npy file in data folder
        #       if the user does not want to scrap new data.
        self.web_scraper.load_data(name)

        self.web_scraper.visualise_house_data()

        self.house_data = self.web_scraper.get_data_dict()

    def scrap_data(self, name):
        # Scraps data from IMMOWEB and stores them in a npy file in data folder

        self.web_scraper.get_web_data()

        self.web_scraper.store_data(name)

        self.web_scraper.visualise_house_data()

        self.house_data = self.web_scraper.get_data_dict()




