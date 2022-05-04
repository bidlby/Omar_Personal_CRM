# Generated by Django 4.0.1 on 2022-05-01 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CRM', '0023_projectinfomodel_createdby'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignprojectmodel',
            name='createdBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignprojectmodel',
            name='userLogin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='a', to=settings.AUTH_USER_MODEL),
        ),
    ]
