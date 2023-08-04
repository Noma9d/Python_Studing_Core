from datetime import datetime


def get_days_from_today(date):
    today = datetime.now()
    today_date = datetime(year = today.year, month = today.month, day = today.day)
    days = date.split('-')
    date_time = datetime(year=int(days[0]), month=int(days[1]), day=int(days[2]))
    result = today_date - date_time
    return result.days
    
    
    
    


print(get_days_from_today('2023-05-15'))