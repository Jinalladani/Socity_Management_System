# Generated by Django 3.2.7 on 2021-10-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20211011_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100, unique=True)),
                ('balance_amount', models.FloatField(max_length=500)),
            ],
        ),
    ]
