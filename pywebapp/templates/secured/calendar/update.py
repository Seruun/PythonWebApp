import datetime

from .... import db
from ....models import CalendarTable

start_year = 2018
start_month = 1
start_day = 1
end_year = 2100
end_month = 12

year = start_year
while year <= end_year:
    if (year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0):
        sj = 1
    else:
        sj = 0
    month = start_month
    while month <= end_month:
        if month in {1, 3, 5, 7, 8, 10, 12}:
            end_day = 31
        elif month in {4, 6, 9, 11}:
            end_day = 30
        else:
            if sj == 1:
                end_day = 29
            else:
                end_day = 28
        day = start_day
        while day <= end_day:
            if month < 10:
                pmonth = '0' + str(month)
            else:
                pmonth = str(month)
            if day < 10:
                pday = '0' + str(day)
            else:
                pday = str(day)
            date_id = str(year) + str(pmonth) + str(pday)
            # print(date_id)
            unf_date = datetime.datetime(year, month, day)
            date = unf_date.strftime('%d.%m.%Y')
            # print(date)
            d = CalendarTable(id=date_id, full_date=date, description=unf_date)
            db.session.add(d)
            db.session.commit()
            day += 1
        print(year, month)
        month += 1
    year += 1
