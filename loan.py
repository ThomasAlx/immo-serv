
class Loan:

    def __init__(self, house_id=None, house_price=None, loan_duration = None):
        self.house_id = house_id
        self.house_price = house_price
        self.loan_duration = loan_duration
        self.status = "proposed"
        self.rate = None
        self.monthly_inst = None
        self.total_amount = None

    def loan_calculator(self):
        self.pick_rate()
        self.calc_total_amount()
        self.calc_month()

    def calc_month(self):
        self.monthly_inst = self.total_amount / self.loan_duration 

    def calc_total_amount(self):
        self.total_amount = (1+self.rate) * self.house_price  

    def pick_rate(self):
        # TODO: updated rates - hardcoded for now:
        if (self.loan_duration<(5*12)):
            self.rate = 0.002
        elif (self.house_price<(10*12)):
            self.rate = 0.007
        else:
            self.rate = 0.01