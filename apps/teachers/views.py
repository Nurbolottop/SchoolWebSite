from django.shortcuts import render
from apps.teachers.models import Teacher
from apps.settings.models import Settings
from apps.contact.models import Contact
# Create your views here.
def teacher_site(request):
    teacher = Teacher.objects.all()
    settings = Settings.objects.latest('id')
    contact = Contact.objects.latest('id')
    context = {
        'teacher' :teacher,
        'settings':settings,
        'contact': contact
    }

    return render(request, 'teachers.html',context)

def teacher_detail(request,id):
    settings = Settings.objects.latest('id')
    teacher = Teacher.objects.get(id = id)
    contact = Contact.objects.latest('id')

    context = {
        'settings':settings,
        'teacher': teacher,
        'contact': contact

    }
    return render(request, 'teacher-single.html', context)