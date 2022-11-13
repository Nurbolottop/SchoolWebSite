from django.shortcuts import render
from apps.classs.models import Classe
from apps.settings.models import Settings
from apps.contact.models import Contact
# Create your views here.
def clase(request):

    classes = Classe.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'settings':settings,
        'contact': contact,
        'classes':classes
    }
    return render(request, 'classes.html', context)
