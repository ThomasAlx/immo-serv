import backendserv

class NewService:

    def __init__(self, house_prices=None):
        self.house_prices = house_prices
        self.proposed_loans  # list of loan objects
        self.accepted_loans
        self.users  # list of user objects
        pass

    def get_loan(self):
        pass

    def set_loan_status(self):
        pass

    def calculate_loan(self):
        # should use imported house_prices
        # create a pytest or an exception for what comes in here
        # invokes loan calculator from class loan
        pass

    def add_loan(self):
        # adds a loan
        pass

    def remove_loan(self):
        pass

    def load_loans(self):
        # uses reader to load user database
        pass
    
    def store_loans(self):
        # uses reader to write in json file
        pass

#-------------------------------------

    def add_user(self):
        # adds user
        pass

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

