# Generated by Django 4.2.1 on 2023-05-23 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_requests_request_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librarian',
            name='requested_books',
        ),
    ]