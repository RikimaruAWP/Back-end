from django import forms

class CreateContactForm(forms.Form):
    name = forms.CharField(label="Nombre del contacto", max_length=100, required=True )
    email = forms.EmailField(label="Correo electrónico", max_length=100, required=True)
    phone = forms.CharField(label="Teléfono", max_length=100, required=True)
    address = forms.CharField(label="Dirección", max_length=200, required=True)
    city = forms.CharField(label="Ciudad", max_length=100, required=True)
    country = forms.CharField(label="País", max_length=100, required=True)  
    
