from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from .models import Book, Student, Librarian, BorrowedBook, RenewedBook


def borrow_book(request):
    books = Book.objects.all()
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST['student']
        book_id = request.POST['book']
        student = Student.objects.get(pk=student_id)
        book = Book.objects.get(pk=book_id)

        if book.available_copies > 0:
            # Check if the student has already borrowed the book
            if BorrowedBook.objects.filter(student=student, book=book).exists():
                return render(request, 'borrow_book.html', {'books': books, 'students': students,
                                                            'error': "Student has already borrowed this book."})

            now = datetime.now()
            return_date = now + timedelta(days=30)

            # Create a BorrowedBook instance to track borrowing
            borrowed_book = BorrowedBook.objects.create(student=student, book=book, borrowed_date=now,
                                                        return_date=return_date)

            # Update the available copies of the book
            book.available_copies -= 1
            book.save()

            return redirect('home')
    return render(request, 'borrow_book.html', {'books': books, 'students': students})


def return_book(request):
    borrowed_books = BorrowedBook.objects.all()
    if request.method == 'POST':
        student_id = request.POST['student_id']
        book_id = request.POST['book_id']
        student = Student.objects.get(user_id=student_id)
        book = Book.objects.get(id=book_id)
        borrowed_book = BorrowedBook.objects.get(student=student, book=book)
        borrowed_book.delete()

        return redirect('book_list')

    return render(request, 'return_book.html', {'borrowed_books': borrowed_books})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        user_id = request.POST['user_id']
        student = Student(name=name, user_id=user_id)
        student.save()
        return redirect('home')
    return render(request, 'add_student.html')


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        total_copies = int(request.POST['total_copies'])
        book = Book(title=title, total_copies=total_copies, available_copies=total_copies)
        book.save()
        return redirect('home')
    return render(request, 'add_book.html')


def renew_book(request):
    students = Student.objects.all()
    if request.method == 'POST':
        student_id = request.POST['student']
        student = Student.objects.get(pk=student_id)
        selected_books = student.borrowed_books.keys()  # Get the book titles

        book_title = request.POST['book']
        if book_title in selected_books:
            renewed_book = RenewedBook(student=student, book=book_title)
            renewed_book.save()

            return redirect('home')
        else:
            error = "Invalid book selection."
            return render(request, 'renew_book.html',
                          {'students': students, 'student': student, 'selected_books': selected_books, 'error': error})

    return render(request, 'renew_book.html', {'students': students})


def add_librarian(request):
    if request.method == 'POST':
        name = request.POST['name']
        user_id = request.POST['user_id']
        librarian = Librarian(name=name, user_id=user_id)
        librarian.save()
        return redirect('home')
    return render(request, 'add_librarian.html')


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

