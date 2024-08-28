from django.shortcuts import render
from .models import Book, Library

l = Library()

# Create your views here.
def home(request):
    return render(request, 'core/base.html')

def list_books(request):
    return render(request, 'core/list.html', {'books': l.books_list})

def form_books(request):
    return render(request, 'core/form.html')

def create_book(request):
    isbn = request.POST.get('isbn')
    title = request.POST.get('title')
    author = request.POST.get('author')
    
    if isbn == '' or title == '' or author == '':
        mensaje = 'Campos vacios'
    else:
        # Instanciamos objeto libro
        b = Book(isbn, title, author)
        # Agregar b objeto libro a libreria
        mensaje = l.agregar_libro(b)
    
    return render(request, 'core/create.html', {'mensaje':mensaje})
    
def delete_book(request, isbn):
    l.eliminar_libro(isbn)
    return render(request, 'core/delete.html')
