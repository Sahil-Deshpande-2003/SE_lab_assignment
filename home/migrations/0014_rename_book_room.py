# Generated by Django 4.2 on 2023-05-18 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_room_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Room',
        ),
    ]
