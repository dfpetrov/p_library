# Generated by Django 2.2.4 on 2019-11-23 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0011_auto_20191120_2224'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RentBooks',
            new_name='BookRent',
        ),
    ]
