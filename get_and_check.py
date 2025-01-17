
def get_and_check_days(day_input):
    try:
        day = int(day_input)
        if 1 <= day <= 31:
            return day
        else:
            return None
    except ValueError:
        return None

def get_and_check_months(month_input):
    try:
        month = int(month_input)
        if 1 <= month <= 12:
            return month
        else:
            return None
    except ValueError:
        return None




