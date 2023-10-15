# Generated by Django 4.2 on 2023-05-18 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='book_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='book_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='room',
            name='book_issue_date',
        ),
        migrations.RemoveField(
            model_name='room',
            name='updated',
        ),
    ]