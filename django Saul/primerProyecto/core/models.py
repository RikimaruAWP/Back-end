from ast import Delete
from enum import auto
from unittest import result
from django.db import models

# Create your models here.

class Book:
    def __init__(self,isbn,title,author) -> None:
        self.isbn=isbn
        self.title= title
        self.author = author
    

class Library:
    def __init__(self) -> None:
        b1 = Book('11', 'Titulo ejemplo', 'Autor ejemplo')
        b2 = Book('22', 'Titulo ejemplo', 'Autor ejemplo')
        b3 = Book('33', 'Titulo ejemplo', 'Autor ejemplo')

        self.books_list = [b1,b2,b3]
     
    #metodo buscar libro
    def searchBook(self, isbn) -> str:
        for b in self.books_list:
            if isbn == b.isbn:
                return b
        return None
    
    #método para agregar un libro al listado
    def adBook(self,book):
        if not isinstance(book,Book):
            return 'Debe agregar libro'
        result = self.searchBook(book.isbn)
        if result is not None:
            return 'El libro ya existe'
        self.books_list.append(book)   
        return 'Libro agregado'
    
    def delete_book(self, isbn):
        result= self.searchBook(isbn)
        print(isbn)
        if result is not None and isinstance(result,Book):
            self.books_list.remove(result)
            return 'El libro se borro correctame'
        else:
            return 'El libro no se encuentra'
    
    def update_book(self, isbn, title, author):
        result= self.searchBook(isbn)
        if result is not None and isinstance(result,Book):
            result.title = title
            result.author = author
            return 'El libro se actualizo correctamente'
        else:
            return 'El libro no se encuentra'

