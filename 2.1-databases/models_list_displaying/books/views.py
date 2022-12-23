from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def catalogue(request):
    template = 'books/catalogue.html'
    book_objects = Book.objects.all()
    book_list = [x for x in book_objects]
    context = {
        'books': book_list
    }
    return render(request, template, context)

def search(request, dt: datetime):
    date = dt.date()
    # book_list = [x for x in Book.objects.all()]
    # paginator = Paginator(book_list, 1)
    # page = paginator.get_page(1)
    print(Book.objects.get(pub_date=date))
    book = Book.objects.get(pub_date=date)
    context = {
        'book': book,
    }
    return render(request, 'books/search.html', context)
