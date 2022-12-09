import matplotlib
from tabulate import tabulate

import pandas as pd

class BackEndService:

    def __init__(self):
        pass

    @staticmethod
    def visualise(obj):
        # just a dummy visualization method

        user_id_lst = []
        house_id_lst = []
        house_price_lst = []
        rate_lst = []
        final_price_lst = []
        month_lst = []
        status_lst = []

        for user in obj.users:

            for loan in obj.loans[user.id]:

                user_id_lst.append(user.id)
                house_id_lst.append(user.house_id_interest)
                house_price_lst.append(obj.house_data[user.house_id_interest])
                rate_lst.append(loan.rate)
                final_price_lst.append(loan.total_amount)
                month_lst.append(loan.monthly_inst)
                status_lst.append(loan.status)

        temp = {}
        temp['User ID'] = user_id_lst
        temp['House ID'] = house_id_lst
        temp['House Price\n[\N{euro sign}]'] = house_price_lst
        temp['Rate'] = rate_lst
        temp['Final Price\n[\N{euro sign}]'] = final_price_lst
        temp['Montlhy Pay\n[\N{euro sign}]'] = month_lst
        temp['Status'] = status_lst

        df = pd.DataFrame(temp)
         
        print("\n\n##############################################################")
        print("Overview:\n")
        print(tabulate(df, headers='keys', tablefmt='psql'))