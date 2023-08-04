from datetime import datetime


def get_str_date(date):
    data = date.split(' ')
    date_time = data[0].split('-')
    x = datetime(year = int(date_time[0]), month = int(date_time[1]), day = int(date_time[2]))

    return x.strftime('%A %d %B %Y')
    
    
    
print(get_str_date('2021-05-27 17:08:34.149Z'))