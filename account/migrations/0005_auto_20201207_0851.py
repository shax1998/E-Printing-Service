# Generated by Django 3.1.3 on 2020-12-07 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_myaccount_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaccount',
            name='dob',
            field=models.DateField(blank=True, null=None),
        ),
    ]