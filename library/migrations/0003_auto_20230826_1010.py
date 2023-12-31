# Generated by Django 3.2.20 on 2023-08-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20230826_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowedbook',
            name='return_date',
        ),
        migrations.AddField(
            model_name='book',
            name='borrowed_dates',
            field=models.ManyToManyField(through='library.BorrowedBook', to='library.Student'),
        ),
        migrations.AddField(
            model_name='borrowedbook',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
