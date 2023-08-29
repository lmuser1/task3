from django.db import models

# Create your models here.


class DateTimeTable(models.Model):
    time = models.DateTimeField()
