# Generated by Django 4.0.1 on 2022-04-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0013_alter_customerinfomodel_gb1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfomodel',
            name='GB1',
            field=models.BooleanField(default=False),
        ),
    ]