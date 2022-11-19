from django.shortcuts import render

from apps.accreditation2.models import AcreditationList2
from apps.settings.models import Settings
from apps.contact.models import Contact
# Create your views here.
def accreditations2(request):
    accreditation = AcreditationList2.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'accreditation':accreditation,
        'settings':settings,
        'contact':contact
    }
    return render(request, 'programmalyk_akkreditatsiya.html', context)

def accreditation_detail2(request,id):
    accreditation = AcreditationList2.objects.get(id = id)
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        ''
        'accreditation':accreditation,
        'settings':settings,
        'contact':contact
    }
    return render(request, 'programmalyk_akkreditatsiya_detail.html', context)