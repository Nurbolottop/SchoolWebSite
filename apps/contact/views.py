from django.shortcuts import render,redirect
from apps.contact.models import Contact,Contact_detail
from apps.settings.models import Settings
from django.core.mail import send_mail

# Create your views here.
def contacts(request):
    contact = Contact.objects.latest('id')
    setting = Settings.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        cont = Contact_detail.objects.create(name = name,email = email,message = message)
        cont.save()
        send_mail(
            'Сообщение от школы',
            f'Саламатсызбы {name}, Жообуңуз үчүн рахмат, биз сиз менен жакында байланышабыз.Сиздин билдирүүңүз: {message} Сиздин почтаңыз: {email}',
            "noreply@somehost.local",
            [email]
        )
        return redirect('index')
        
    context ={
        'contact':contact,
        'setting':setting
    }
    return render(request, 'contacts.html',context)
