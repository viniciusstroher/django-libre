# Generated by Django 3.2.8 on 2021-10-26 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20211025_2101'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Tickets',
        ),
    ]