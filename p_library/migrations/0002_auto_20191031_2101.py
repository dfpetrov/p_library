# Generated by Django 2.2.6 on 2019-10-31 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='birth_day',
            new_name='birth_year',
        ),
    ]
