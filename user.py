from inout import *
from loan import *

class User:

    def __init__(self, id=None, house_id_interest=None):
        self.id = id
        self.house_id_interest = house_id_interest
        self.loans = []

    def set_loan(self, house_id, price, duration, loan_id):
        self.loans.append(Loan(house_id, price, duration, id=loan_id))

    def calc_loan(self, loan_id):
        self.loans[loan_id].loan_calculator()

    def set_user(self):
        # should use reader to save data
        pass

    def get_user(self):
        # should use reader to store data
        pass

    def get_loan(self, loan_id):
        return self.loans[loan_id]