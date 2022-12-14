
# ONLY USED TO CREATE THE INTERFACE IN MAIN TO USE THE NEW SERVICE

################################################
# Helper functions
################################################

def new_choice_question(answer, exit_choice_flag, curr_loan_id):
    if (answer=='y'):
        exit_choice_flag = True
    else:
        exit_choice_answer = int(input("\nPress 1 to continue \ 0 to exit:\t"))
        exit_choice_flag = True
        if (exit_choice_answer):
            exit_choice_flag = False
    curr_loan_id += 1
    return curr_loan_id, exit_choice_flag

def new_user_question(curr_user_id, exit_flag):
    # user input: ask for new user or exit
    new_user_q = int(input("\nPress 1 for new user, or 0 to exit:\t"))
    if (new_user_q):
        curr_user_id += 1
    else:
        exit_flag = True
    return curr_user_id, exit_flag

def input_house_id(nS):
    flag = True
    while (flag):
        house_id = int(input("\nPlease input property id (integer from %d to %d) :\t"% (0,len(nS.house_data)-1)) )
        flag = False
        if (house_id>len(nS.house_data)-1):
            print("\nInvalid id, try again:\n")
            flag = True

    return house_id