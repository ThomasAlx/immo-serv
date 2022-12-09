import backendserv
from loan import Loan
from user import User

class NewService:

    def __init__(self, house_data=None):
        self.house_data = house_data
        self.users = []
        self.proposed_loans = {}  # dictionary of lists  
        self.accepted_loans = {}  # dictionary
        pass

    def prompt_choice(self, user_id):

        loan_duration = int(input("\nInsert loan duration in months:\t"))

        proposal = self.calculate_loan(loan_duration, user_id)

        # TODO: finish that
        # self.visualise_proposal(proposal)

        answer = int(input("\nPress 1 for yes, or 0 for no:\t"))

        self.add_loan(proposal, answer, user_id)

        return answer

    def visualise_proposal(proposal):
        pass

    def calculate_loan(self, duration,user_id):
        # Input:
        #       - duration: duration of loan in months
        #       - user_id:  id of user in self.users list
        # Output:
        #       - proposal: loan instance 

        house_price = self.house_data[self.users[user_id].house_id_interest]
        
        # loan interest
        proposal = Loan(house_price, duration)

        # calculate loan specifics
        proposal.loan_calculator()

        # return loan object
        return proposal

    def add_loan(self, proposal, answer, user_id):
        # adds a loan to proposed list
        self.proposed_loans[user_id].append(proposal)

        # if accepted, it also adds it to the accepted list
        if (answer):
            self.users[user_id].chose_loan_flag = True
            self.accepted_loans[user_id] = proposal

    def remove_loan(self):
        pass

    def load_loans(self):
        # uses reader to load user database
        pass
    
    def store_loans(self):
        # uses reader to write in json file
        pass

    def get_loan(self):
        pass

    def set_loan_status(self):
        pass

#-------------------------------------

    def add_user(self, new_user):
        self.users.append(new_user)
        self.proposed_loans[new_user.id] = []

    def get_user(self):
        pass

    def load_users(self):
        # uses reader to load user database
        pass
    
    def store_users(self):
        # uses reader to write in json file
        pass

    def remove_user(self):
        pass

#-------------------------------------

    def visualize(self):
        # invokes backend service
        pass



