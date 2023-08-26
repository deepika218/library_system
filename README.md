# Library System

This Project will create Students, create Librarian, Add Books, List Books, Borrow Book, and Return the Book.
This project is developed using Python, Django and Sqlite database.

## Features

- It contains four Templates's. 1.Home, 2.Add Book, 3.Add Student, 4.Add Librarian, 5.Borrow Book, 6.Return Book, and 7. Book List

## Tech

This project uses multiple open source to make setup:

- [Python] - As Backend Language
- [Django] - As Backend Framework
- [faker] - For creating fake data to test while development
- [Sqlite Database] - As light-weight and default supported databases

## Installation

This project requires [Python3.9](https://www.python.org/downloads/release/python-360/)

Install the dependencies and devDependencies and start the server.

```sh
cd library_system
pip3 install requirements.txt
python manage.py runserver
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| API | Method | Description | URL | Payload |
| ------ | ------ | ------ | ------ | ------ |
| Home | GET | For Fetching Home page and loading book list data | [http://127.0.0.1:8000] |  |
| Add Student |  POST | For Student Add | [http://127.0.0.1:8000/library/add_student/] | {"name": "test1", "user_id":"101"} |
| Add Book |  POST | For Book Add | [http://127.0.0.1:8000/library/add_book/] | {"title": "book1", "total_copies":10} |
| List All Book |  GET | For Listing Book | [http://127.0.0.1:8000/library/book/] |  |
| Add Librarian |  POST | For Librarian Add | [http://127.0.0.1:8000/library/add_librarian/] | {"name": "lib101", "user_id":"201"} |
| Borrow Book |  POST | For Borrowing Book | [http://127.0.0.1:8000/library/borrow_book/] | {"student": "101", "book":"1"} |
| List Borrowed Books |  GET | For Listing all Borrowed Books | [http://127.0.0.1:8000/library/return_book/] | |
| Return Book |  POST | For Returning Book | [http://127.0.0.1:8000/library/return_book/] | {"student_id": "101", "book_id":"1"} |


Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```
