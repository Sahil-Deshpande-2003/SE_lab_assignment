# Generated by Django 4.2.1 on 2023-05-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_student_requested_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='requested_books',
            field=models.TextField(blank=True, null=True),
        ),
    ]
