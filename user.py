import reader

class User:

    def __init__(self, id=None, house_id_interest=None):
        self.id = id
        self.house_id_interest = house_id_interest
        self.chose_loan_flag = None
        self.choices = []
        self.answers = []

    def set_user(self):
        # should use reader to save data in json ? files
        pass

    def get_user(self):
        # should use reader to store data
        pass