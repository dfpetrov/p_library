# Generated by Django 2.2.6 on 2019-11-01 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_book_edition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='edition',
        ),
    ]
