from datetime import date


def get_days_in_month(month, year):
    if year % 4 == 0 and month == 2:
        result = 29
    elif year % 4 != 0 and month == 2:
        result = 28
    elif month in (1, 3, 5, 7, 8, 10, 12):
        result = 31
    else:
        result = 30

    return result

        
    
