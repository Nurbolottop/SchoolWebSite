
from django.shortcuts import render
from apps.settings.models import Settings, Slide,Title

from apps.contact.models import Contact
from apps.News.models import New 
# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    slide = Slide.objects.latest('id')
    title = Title.objects.latest('id')
    news = New.objects.all()
    
    context ={
        'settings':settings,
        'contact':contact,
        'slide':slide,
        'news': news,
        'title':title
    }
    return render(request,'index.html',context)



