from django.shortcuts import render
from apps.News.models import New 
from apps.settings.models import Settings
from apps.contact.models import Contact
# Create your views here.
def new_site(request):
    new = New.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'settings':settings,
        'contact': contact,
        'new':new

    }
    return render(request, 'blog.html', context)

def new_post(request,id):
    new = New.objects.get(id =id)
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'settings':settings,
        'contact': contact,
        'new':new
    }
    return render(request, 'post.html',context)