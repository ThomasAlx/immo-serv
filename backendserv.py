from tabulate import tabulate
import pandas as pd

#############################################
# DUMMY BACKEND SERVICE
#############################################

class BackEndService:

    def __init__(self):
        pass

    @staticmethod
    def visualise(obj):

        user_id, house_id, house_price, rate, final_price, month, status = [], [], [], [], [], [], []

        for user in obj.users:

            for loan in user.loans:

                user_id.append(user.id)
                house_id.append(user.house_id_interest)
                house_price.append(obj.house_data[user.house_id_interest])
                rate.append(loan.rate)
                final_price.append(loan.total_amount)
                month.append(loan.monthly_inst)
                status.append(loan.status)

            # add empty line
            BackEndService.add_empty_line([user_id, house_id,
                        house_price, rate, final_price, month, status])

        temp = {}
        temp['User ID'] = user_id
        temp['House ID'] = house_id
        temp['House Price\n[\N{euro sign}]'] = house_price
        temp['Rate'] = rate
        temp['Final Price\n[\N{euro sign}]'] = final_price
        temp['Montlhy Payment\n[\N{euro sign}]'] = month
        temp['Status'] = status

        df = pd.DataFrame(temp)
         
        print("\n\n##############################################################")
        print("Overview:\n")
        print(tabulate(df, headers='keys', tablefmt='psql'))

    @staticmethod
    def add_empty_line(lists):
        for lst in lists:
            lst.append("")