from datetime import datetime

from ....models import DatesTable

# Datum heute --> Defaul Anzeige beim öffnen des Kalenders!
unf_date_today = datetime.now()
date_today = unf_date_today.strftime('%d.%m.%Y')


## Debugger ##
# print(date_today)


def get_Year(datum):
    year = datum.strftime('%Y')
    return year


def get_Month(datum):
    month = datum.strftime('%m')
    return month


def get_Day(datum):
    day = datum.strftime('%d')
    return day


def get_DateID(datum):
    dateID = datum.strftime('%Y%m%d')
    return dateID


def get_Date(ID):
    datum = DatesTable.get(ID)
    return datum
