################################################
# Helper functions
################################################

def new_choice_question(answer, exit_choice_flag):
    if (answer=='y'):
        exit_choice_flag = True
    else:
        exit_choice_answer = int(input("\nPress 0 to continue, 1 to exit choice:\t"))
        if (exit_choice_answer):
            exit_choice_flag = True
    return exit_choice_flag

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
        house_id = int(input("\nPlease input property id :\t"))
        flag = False
        if (house_id>len(nS.house_data)-1):
            print("\nInvalid id, try again:\n")
            flag = True

    return house_id