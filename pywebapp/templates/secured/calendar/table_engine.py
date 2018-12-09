from flask_table import Table, Col
from ....models import DatesTable, Room


def CalendarItems(date_id):
    items_calendar = DatesTable.query.filter_by(date_id=date_id)
    table_calendar = CalendarTable(items_calendar)

    print(table_calendar.__html__())
    return table_calendar.__html__()


class DateTable(Table):
    uhrzeit = Col('Uhrzeit')
    room_id1 = Col('Raum 1')
    room_id2 = Col('Raum 2')


class CalendarTable(Table):
    date_id = Col('Datum_ID')
    date = Col('Datum')


class Dates(object):
    r = Room.query.all()

    start_time = Col('Uhrzeit')
    if r.room_id == 1:
        room_id = Col('Raum 1')
    elif r.room_id == 2:
        room_id = Col('Raum 2')
    else:
        raise Warning('Falsche Raumnummer!')

