# Generated by Django 4.0.1 on 2022-05-01 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0027_alter_commentsmodel_gb1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentsmodel',
            name='customerId',
        ),
    ]
