# Generated by Django 3.2.7 on 2021-09-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210929_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='society',
            name='password',
        ),
        migrations.AlterField(
            model_name='society',
            name='moblie_no',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]