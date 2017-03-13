days_in_month_dict = {"January": 31, "February": 28, 
                      "March": 31, "April": 30,
                      "May": 31, "June": 30, 
                      "July": 31, "August": 31,
                      "September": 30, "October": 31,
                      "November": 30, "December": 31}

def is_leap_year(year):
    '''
    Return if year is lip or not
    '''
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    '''
    Return number of days in a given month

    print(simplecalendar.days_in_month(2017, 'February'))
    return 28
    '''
    if is_leap_year(year) and month == "February":
        return 28

    try: 
        #attempt to get value from dictionary 
        return days_in_month_dict[month]
    except KeyError:
        #key does not exist, so we caught the error
        return None
