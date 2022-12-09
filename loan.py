
class Loan:

    def __init__(self, house_price=None, duration = None):
        self.duration = duration
        self.house_price = house_price
        self.status = "proposed"
        self.interest = None
        self.monthly_inst = None

    def loan_calculator(self):
        self.pick_interest()
        self.calc_total_amount()
        self.calc_month()

    def calc_month(self):
        self.monthly_inst = self.total_amount / self.duration 

    def calc_total_amount(self):
        self.total_amount = (1+self.interest) * self.house_price  

    def pick_interest(self):
        # TODO: updated interests - hardcoded for now:
        if (self.house_price>1000000):
            self.interest = 0.002
        elif (self.house_price>500000):
            self.interest = 0.007
        else:
            self.interest = 0.01