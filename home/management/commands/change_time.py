from django.core.management.base import BaseCommand
from home.models import DateTimeTable
from pytz import timezone


def pst_to_utc(date_object):
    converted_date = date_object.astimezone(timezone('UTC'))
    return converted_date


def utc_to_pst(date_object):
    converted_date = date_object.astimezone(timezone('US/Pacific'))
    return converted_date


class Command(BaseCommand):
    help = 'Change Time'

    def handle(self, *args, **kwargs):

        # making list of IDs of object present in DateTimeTable in database
        # then iterating over these IDs
        items = DateTimeTable.objects.all()
        objects_ids = []
        for item in items:
            objects_ids.append(item.id)

        # getting the counter from the file which was last saved
        with open("file.txt", "r") as f:
            counter = f.read()
        intcounter = int(counter)

        # changing time
        for i in objects_ids[intcounter:intcounter+10]:
            dt = DateTimeTable.objects.get(pk=i)
            if 'PDT' in dt.tzname():
                new_time = pst_to_utc(dt)
                dt.time = new_time
                dt.save()
            else:
                new_time = utc_to_pst(dt)
                dt.time = new_time
                dt.save()

        # For updating counter in file
        with open("file.txt", "w") as f:
            if intcounter > 90:
                f.write('0')  # for resetting the counter to zero
            else:
                intcounter = intcounter + 10
                f.write(str(intcounter))
