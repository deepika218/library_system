from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()
    borrowed_dates = models.ManyToManyField('Student', through='BorrowedBook')

    def __str__(self):
        return self.title


class User(models.Model):
    USER_TYPES = [
        ('Student', 'Student'),
        ('Librarian', 'Librarian'),
    ]

    user_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.name


class Student(User):
    borrowed_books = models.ManyToManyField(Book, through='BorrowedBook', related_name='borrowed_books_students')
    renewed_books = models.ManyToManyField(Book, through='RenewedBook', related_name='renewed_books_students')


class Librarian(User):
    pass


class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField()
    return_date = models.DateTimeField()


class RenewedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    renew_count = models.PositiveIntegerField(default=0)


class LibrarySystem(models.Model):
    books = models.ManyToManyField(Book)
    users = models.ManyToManyField(User, related_name='library_system_users')
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    def __str__(self):
        return "Library System"
