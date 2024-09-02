from turtle import title
from django.shortcuts import render
from .models import Library, Book
l=Library()
# Create your views here.

def home(request):
    return render(request, 'core/base.html')

def crear(request):
    return render(request, 'core/form.html' )

def create_books(request):
    isbn = request.POST.get('isbn')
    title = request.POST.get('title')
    author = request.POST.get('author')
    if isbn == '' or title == '' or author =='':
        mensaje = 'Campo vacio'
    else:
        b=Book(isbn,title,author)
        mensaje = l.adBook(b)
    
    return render (request, 'core/create.html', {'mensaje':mensaje})

def list(request):
    return render(request, 'core/list.html',{'books':l.books_list})


def confirm_delete(request, isbn):
    print(isbn)
    return render(request, 'core/confirm_delete.html',{'isbn':isbn})

def elimanar_book(request):
    isbn = request.POST.get('isbn')
    if isbn == '':
        mensaje = 'Se ha producido un error'
    else:  
        mensaje = l.delete_book(isbn)
    return render (request, 'core/delete.html', {'mensaje':mensaje})

def update_view(request, isbn):
    return render(request, 'core/update.html', {'isbn':isbn})


def update_message(request):

    isbn = request.POST.get('isbn')
    title = request.POST.get('title')
    author = request.POST.get('author')
    if isbn == '' or title == '' or author =='':
        mensaje = 'Campo vacio'
    else:
        mensaje = l.update_book(isbn, title, author)
    return render(request, 'core/mensaje_update.html', {'mensaje':mensaje})

  

