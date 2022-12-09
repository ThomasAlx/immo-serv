from backendserv import BackEndService
from loan import Loan
from user import User
import pandas as pd
from tabulate import tabulate

class NewService:

    def __init__(self, house_data=None):
        self.house_data = house_data
        self.users = []
        self.loans = {}  # dictionary of lists
        pass

    def prompt_choice(self, user_id):

        loan_duration = int(input("\nInsert loan duration in months:\t"))

        proposal = self.calculate_loan(loan_duration, user_id)

        self.visualise_proposal(proposal, user_id)

        answer = int(input("\nPress 1 for yes, or 0 for no:\t"))

        self.add_loan(proposal, answer, user_id)

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

    def add_loan(self, proposal, answer, user_id):
        # if accepted, it also adds it to the accepted list
        if (answer):
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

    def add_user(self, new_user):
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

    def visualise(self):
        # invokes backend service
        BackEndService.visualise(self)



