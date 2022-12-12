from inout import *
from loan import *

class User:

    def __init__(self, id=None, house_id_interest=None):
        self.id = id  # integer
        self.house_id_interest = house_id_interest  # string
        self.loans = []  # list of "loan" objects

    def set_loan(self, house_id, price, duration, loan_id):
        # creates a Loan instance
        # sets its parameters
        # includes it in loans attribute
        self.loans.append(Loan(house_id, price, duration, id=loan_id))

    def calc_loan(self, loan_id):
        # invokes the loan calculator member function
        self.loans[loan_id].loan_calculator()

    def store_user(self):
        # should use inout to save data
        pass

    def get_user(self):
        # should use inout to store data
        pass

    def get_loan(self, loan_id):
        # returns a loan based on its id
        return self.loans[loan_id]