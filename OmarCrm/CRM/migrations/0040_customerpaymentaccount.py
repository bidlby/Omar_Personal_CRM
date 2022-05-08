# Generated by Django 4.0.1 on 2022-05-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0039_alter_paymentsmodel_gb1'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerPaymentAccount',
            fields=[
                ('transactionDate', models.DateField(editable=False)),
                ('customerId', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('customerName', models.CharField(editable=False, max_length=100)),
                ('paymenttype', models.CharField(editable=False, max_length=50)),
                ('paymentRef', models.CharField(editable=False, max_length=200)),
                ('type', models.CharField(editable=False, max_length=200)),
                ('credit', models.IntegerField(editable=False)),
                ('debit', models.IntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'CustomerAccountBalance',
                'verbose_name_plural': 'CustomerAccountBalances',
                'db_table': 'CustomerAccountBalance',
                'ordering': ['transactionDate'],
                'managed': False,
            },
        ),
    ]