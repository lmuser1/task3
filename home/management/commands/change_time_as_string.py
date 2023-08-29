from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from home.models import DateTimeTable



def pst_to_utc(str):
    l = list(str)
    hour = l[13]+l[14]
    int(hour)
    new_hour = hour + 8
    str(new_hour)
    l1= list(new_hour)
    
    l[24] = 'U'
    l[25] = 'T'
    l[26] = 'C'



def utc_to_pst():
    pass


class Command(BaseCommand):
    help = 'Create dummy users'

    def handle(self, *args, **kwargs):
        items = DateTimeTable.objects.all()
        objects_ids = []
        for item in items:
            objects_ids.append(item.id)

        with open("file.txt", "w+") as f:
            counter = f.read()
        
        int(counter)

        for i in range(counter,counter+10):
            dt = DateTimeTable.objects.get(pk=i)
            if 'UTC' in dt.time:
                utc_to_pst(dt.time)
            else:
                pst_to_utc()

        with open("file.txt", "w+") as f:
            f.write(str(+10))
        
