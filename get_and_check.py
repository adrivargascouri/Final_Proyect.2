
def get_and_check_days(): 
    while True:
        try:
            day = int(input("Enter the day of the month you were born (1-31): "))
            if 1 <= day <= 31: 
                return day
            else:
                print("Invalid day. Please enter a number between (1-31).")
                print("")
        except ValueError:
            print("Input not valid, please enter a number between (1-31).")
            print("")
                


def get_and_check_months():
    while True:
        try:
            month = int(input("Enter the month of your birth (1-12): "))
            if 1 <= month <= 12:
                return month
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Input not valid, please enter a number between (1-12).")
            print("")
