from django.core.management.base import BaseCommand
from home.models import DateTimeTable
from pytz import timezone
from datetime import datetime
import pytz


def time_in_pst():
    date = datetime.now(tz=pytz.utc)                    # used to get current time in UTC
    date = date.astimezone(timezone('US/Pacific'))   # used to convert the given timezone in PST
    date_format = '%m_%d_%Y___%H_%M_%S___%Z'
    pstDateTime = date.strftime(date_format)
    print(pstDateTime)
    return pstDateTime


class Command(BaseCommand):
    help = 'Add datetime Entries'

    def add_arguments(self, parser):
        parser.add_argument('no_of_entries', type=int, help='Indicates the number of datetime entries to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['no_of_entries']
        date = datetime.now()
        timepst = date.astimezone(timezone('US/Pacific'))
        print(timepst)
        for i in range(total):
            DateTimeTable.objects.create(time=timepst)

        self.stdout.write("Added %i entries" % total)
