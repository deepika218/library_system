from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_list, name='book_list'),
    path('', views.home, name='home'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_librarian/', views.add_librarian, name='add_librarian'),
    path('borrow_book/', views.borrow_book, name='borrow_book'),
    path('return_book/', views.return_book, name='return_book'),
]
