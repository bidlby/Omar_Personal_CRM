# Generated by Django 4.0.1 on 2022-04-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0015_alter_customerinfomodel_gb1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfomodel',
            name='GB1',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
