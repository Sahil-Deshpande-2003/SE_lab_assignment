# Generated by Django 4.2.1 on 2023-05-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_librarian_issued_books_student_held_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='id',
        ),
        migrations.AddField(
            model_name='requests',
            name='request_id',
            field=models.CharField(default=1, max_length=200, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
