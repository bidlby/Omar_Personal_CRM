# Generated by Django 4.0.1 on 2022-04-09 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0008_alter_projectinfomodel_startdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignprojectmodel',
            name='assignDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]