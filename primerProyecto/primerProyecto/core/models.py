from unittest import result
from django.db import models

# Create your models here.
class Book:
    def __init__(self, isbn, title, author) -> None:
        self.isbn = isbn
        self.title = title
        self.author = author
        
class Library:
    def __init__(self) -> None:
        b1 = Book('1234', 'El principito', 'Antoine de Saint-Exupéry')
        b2 = Book('5678', 'El alquimista', 'Paulo Coelho')
        b3 = Book('9101', 'El arte de la guerra', 'Sun Tzu')
        self.books_list = [b1, b2, b3]
        
    # Methodos para libreria
    
    # Metodo para buscar libros
    def buscar_libro(self, isbn): # 1234
        # recorrer listado para encontrar libro con isbn entregado
        for b in self.books_list:
            if isbn == b.isbn: # 1234
                return b # retorna un libro
        return None
    
    # Metodo para agregar libro a listado
    def agregar_libro(self, book) -> str:
        if not isinstance(book, Book):
            return 'Debe agregar libros'
        
        result = self.buscar_libro(book.isbn)
        
        if result is not None:
            return 'Libro ya existe'
                    
        # Agregando libro a listado
        self.books_list.append(book)
        return 'Libro agregado'

    def eliminar_libro(self, isbn):
        result = self.buscar_libro(isbn)
        if result is None:
            return 'Libro no encontrado'
        else:
            self.books_list.remove(result)
            return 'Libro eliminado'
