# Generated by Django 4.2 on 2023-05-18 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_book_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='book_name',
        ),
    ]
