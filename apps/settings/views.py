
from django.shortcuts import render
from apps.settings.models import Lessons, Settings, Slide,Title
from apps.about.models import About

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


def about(request):
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    lesson = Lessons.objects.all()
    title = Title.objects.latest('id')
    about = About.objects.latest('id')

    context = {
        'settings':settings,
        'contact':contact,
        'lesson':lesson,
        'title':title,
        'about':about

    }
    return render(request, 'about.html', context)
