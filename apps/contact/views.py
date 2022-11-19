from django.shortcuts import render,redirect
from django.core.mail import send_mail
    
from apps.contact.models import Contact,Contact_detail
from apps.settings.models import Settings

# Create your views here.
def contacts(request):
    contact = Contact.objects.latest('id')
    setting = Settings.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact_detail.objects.create(name = name,email = email,message = message)
        send_mail(
            f'{message}',

            f'Саламатсызбы {name}, Жообуңуз үчүн рахмат, биз сиз менен жакында байланышабыз.Сиздин билдирүүңүз: {message} Сиздин почтаңыз: {email}',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')
        
    context ={
        'contact':contact,
        'setting':setting
    }
    return render(request, 'contacts.html',context)
