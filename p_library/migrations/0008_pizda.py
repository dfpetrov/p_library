# Generated by Django 2.2.6 on 2019-11-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_book_edition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
            ],
        ),
    ]
