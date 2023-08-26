import os
from datetime import timedelta

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')
django.setup()

from library.models import Book, Student, Librarian, BorrowedBook, RenewedBook

fake = Faker()


def generate_fake_books(n):
    for _ in range(n):
        title = fake.sentence(nb_words=6)[:-1]  # Generate a title with 3 words
        total_copies = fake.random_int(min=1, max=20)
        Book.objects.create(title=title, total_copies=total_copies, available_copies=total_copies)


def generate_fake_users(n_students, n_librarians):
    for _ in range(n_students):
        name = fake.name()
        user_id = fake.unique.uuid4()[:8].upper()
        Student.objects.create(name=name, user_id=user_id)

    for _ in range(n_librarians):
        name = fake.name()
        user_id = fake.unique.uuid4()[:8].upper()
        Librarian.objects.create(name=name, user_id=user_id)


def generate_fake_borrowed_books():
    students = Student.objects.all()
    books = Book.objects.all()

    for student in students:
        for _ in range(fake.random_int(min=0, max=5)):
            book = fake.random_element(books)
            borrow_date = fake.date_time_this_year()
            return_date = borrow_date + timedelta(days=fake.random_int(min=7, max=30))
            BorrowedBook.objects.create(student=student, book=book, borrow_date=borrow_date, return_date=return_date)


def generate_fake_renewed_books():
    students = Student.objects.all()
    books = Book.objects.all()

    for student in students:
        for _ in range(fake.random_int(min=0, max=3)):
            book = fake.random_element(books)
            RenewedBook.objects.create(student=student, book=book, renew_count=fake.random_int(min=1, max=2))


if __name__ == '__main__':
    generate_fake_books(200)  # Generate 10 fake books
    generate_fake_users(40, 25)  # Generate 5 fake students and 2 fake librarians
    generate_fake_borrowed_books()  # Generate fake borrowed books
    generate_fake_renewed_books()  # Generate fake renewed books
