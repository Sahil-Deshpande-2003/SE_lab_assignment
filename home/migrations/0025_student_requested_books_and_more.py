# Generated by Django 4.2.1 on 2023-05-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_librarian_requested_books_alter_room_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='requested_books',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='requested_books',
            field=models.JSONField(blank=True, null=True),
        ),
    ]