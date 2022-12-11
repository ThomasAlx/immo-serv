from backendserv import BackEndService
from loan import Loan
from user import User
import pandas as pd
from tabulate import tabulate
from immoscraper import ImmoScraper

class NewService:

    def __init__(self, house_data=None):
        self.house_data = house_data
        self.users = []
        self.loans = {}  # dictionary of lists
        self.web_scraper = None
        pass

    def propose_loan(self, user_id, loan_duration):
        # main function of new service

        proposal = self.calculate_loan(loan_duration, user_id)

        self.visualise_proposal(proposal, user_id)

        # user input to accept calculated loan
        answer = self.get_answer()

        self.add_loan(proposal, answer, user_id)

        return answer

    def calculate_loan(self, duration,user_id):
        # Input:
        #       - duration: duration of loan in months
        #       - user_id:  id of user in self.users list
        # Output:
        #       - proposal: loan instance 

        house_id = self.users[user_id].house_id_interest
        house_price = self.house_data[house_id]
        
        # loan interest
        proposal = Loan(house_id, house_price, duration)

        # calculate loan specifics
        proposal.loan_calculator()

        # return loan object
        return proposal

    def get_answer(self):
        check_flag = True
        while (check_flag):
            answer = input("\nTo accept proposal press: 'y' / To cancel press: 'n'\t")
            check_flag = False
            if (answer!='n' and answer!='y'):
                print("\nPlease enter a valid option.")
                check_flag = True
        return answer

    def visualise_proposal(self, proposal, user_id):
        df = pd.DataFrame({'User ID'      :   [self.users[user_id].id],
             'House ID'     :   [proposal.house_id],
             'House Price\n[\N{euro sign}]'  :   [proposal.house_price],
             'Loan Duration\n[months]':   [proposal.duration],
             'Rate'         :   [proposal.rate],
             'Final Price\n[\N{euro sign}]'  :   [proposal.total_amount],
             'Montlhy Pay\n[\N{euro sign}]'  :   [proposal.monthly_inst]}) 
        print("\n\n##############################################################")
        print("New Proposal:\n")
        print(tabulate(df, headers='keys', tablefmt='psql'))
        
    def add_loan(self, proposal, answer, user_id):
        # if accepted, it also adds it to the accepted list
        if (answer=='y'):
            self.users[user_id].chose_loan_flag = True
            proposal.status = "accepted"

        # adds a loan to proposed list
        self.loans[user_id].append(proposal)


            # self.accepted_loans[user_id] = proposal

    # def remove_loan(self):
    #     pass

    # def load_loans(self):
    #     # uses reader to load user database
    #     pass
    
    # def store_loans(self):
    #     # uses reader to write in json file
    #     pass

    # def get_loan(self):
    #     pass

    # def set_loan_status(self):
    #     pass

#-------------------------------------

    def add_user(self, curr_user_id, input_house_id):
        keys = list(self.house_data.keys())
        new_user = User(id=curr_user_id, house_id_interest=keys[input_house_id])
        self.users.append(new_user)
        self.loans[new_user.id] = []

    # def get_user(self):
    #     pass

    # def load_users(self):
    #     # uses reader to load user database
    #     pass
    
    # def store_users(self):
    #     # uses reader to write in json file
    #     pass

    # def remove_user(self):
    #     pass

#-------------------------------------

    def visualise_overview(self):
        # invokes backend service
        BackEndService.visualise(self)

#-------------------------------------

    def set_web_scraper(self, url, folder):
        self.web_scraper = ImmoScraper(base_url=url, data_folder=folder)

    def load_house_data(self):

        self.web_scraper.load_data()

        self.web_scraper.visualise_house_data()

        self.house_data = self.web_scraper.get_data_dict()

        return self.house_data, list(self.house_data.keys())

    def scrap_data(self):

        self.web_scraper.get_web_data()

        self.web_scraper.store_data()




