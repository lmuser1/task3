from django.contrib import admin
from home.models import DateTimeTable

# Register your models here.


@admin.register(DateTimeTable)
class DateTimeTableAdmin(admin.ModelAdmin):
    list_display = ['time', 'id']
