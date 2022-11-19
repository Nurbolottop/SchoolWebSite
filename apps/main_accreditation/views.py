from django.shortcuts import render

from apps.settings.models import Settings
from apps.contact.models import Contact
# Create your views here.

def main_accreditations(request):
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')

    context = {
        'settings':settings,
        'contact': contact
    }
    return render(request, 'main_accreditation.html', context)