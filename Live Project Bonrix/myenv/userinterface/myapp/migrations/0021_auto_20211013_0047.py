# Generated by Django 3.2.7 on 2021-10-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_balancevalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income_expense_ledgervalue',
            name='remark',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='income_expense_ledgervalue',
            name='voucherNo_or_invoiceNo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]