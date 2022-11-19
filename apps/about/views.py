from django.shortcuts import render


from apps.about.models import About
from apps.settings.models import Settings,Title
from apps.contact.models import Contact


# Create your views here.

def about(request):
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    about = About.objects.latest('id')
    title = Title.objects.latest('id')

    context = {
        'settings':settings,
        'contact':contact,
        'about':about,
        'title':title


    }
    return render(request, 'about.html', context)