# Generated by Django 4.0.1 on 2022-04-30 11:18

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0021_customerinfomodel_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsmodel',
            name='CreatedBy',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=50),
        ),
    ]
