# Generated by Django 4.0.1 on 2022-05-01 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0026_remove_commentsmodel_createdby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='GB1',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
