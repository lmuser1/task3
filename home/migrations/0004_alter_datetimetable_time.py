# Generated by Django 4.0.6 on 2022-07-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_datetimetable_yo_datetimetable_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datetimetable',
            name='time',
            field=models.TextField(),
        ),
    ]
