from django.shortcuts import render

from apps.accreditation1.models import AcreditationList1
from apps.settings.models import Settings
from apps.contact.models import Contact
# Create your views here.

def accreditations1(request):
    accreditation = AcreditationList1.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'settings':settings,
        'contact':contact
    }
    return render(request, 'institutsionaldyk_akkreditatsiya.html', context)

def accreditation_detail1(request,id):
    accreditation = AcreditationList1.objects.get(id = id)
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        ''
        'accreditation':accreditation,
        'settings':settings,
        'contact':contact
    }
    return render(request, 'institutsionaldyk_akkreditatsiya_detail.html', context)