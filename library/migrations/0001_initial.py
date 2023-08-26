# Generated by Django 3.2.20 on 2023-08-26 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('total_copies', models.PositiveIntegerField()),
                ('available_copies', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('Student', 'Student'), ('Librarian', 'Librarian')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.user')),
            ],
            bases=('library.user',),
        ),
        migrations.CreateModel(
            name='RenewedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renew_count', models.PositiveIntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.user')),
                ('borrowed_books', models.ManyToManyField(related_name='borrowed_books_students', through='library.BorrowedBook', to='library.Book')),
                ('renewed_books', models.ManyToManyField(related_name='renewed_books_students', through='library.RenewedBook', to='library.Book')),
            ],
            bases=('library.user',),
        ),
        migrations.AddField(
            model_name='renewedbook',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.student'),
        ),
        migrations.CreateModel(
            name='LibrarySystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(to='library.Book')),
                ('users', models.ManyToManyField(related_name='library_system_users', to='library.User')),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.librarian')),
            ],
        ),
        migrations.AddField(
            model_name='borrowedbook',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.student'),
        ),
    ]
