# Generated by Django 3.2 on 2023-05-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20230501_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='book_category',
            field=models.CharField(default='DEFAULT VALUE', max_length=200),
        ),
    ]