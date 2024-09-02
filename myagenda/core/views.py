from django.shortcuts import render, redirect
from .forms import CreateContactForm
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_contact(request):
    if request.method == 'GET':
        return render(request, 'create_contact.html', {'form': CreateContactForm()})
    else:
        form = CreateContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=request.POST["name"],
                email=request.POST["email"],
                phone=request.POST["phone"],
                address=request.POST["address"],
                city=request.POST["city"],
                country=request.POST["country"]
            )
            return redirect('list_contacts')
        else:
            return render(request, 'core/create_contact.html', {'form': form})


def list_contacts(request): 
    contacts = Contact.objects.all()
    return render(request, 'core/list_contacts.html', {'contacts': contacts})