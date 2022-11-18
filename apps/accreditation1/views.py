from django.shortcuts import render

from apps.accreditation1.models import AcreditationList1

# Create your views here.

def accreditations(request):
    accreditation = AcreditationList1.objects.all()

    context = {
        'accreditation':accreditation
    }
    return render(request, 'accreditation.html', context)