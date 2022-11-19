"""SITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from apps.settings.views import index

from apps.News.views import new_site,new_post

from apps. about.views import about

from apps.contact.views import contacts

from apps.teachers.views import teacher_site,teacher_detail

from apps.classs.views import clase

from apps. accreditation1.views import accreditations1,accreditation_detail1

from apps. accreditation2.views import accreditations2,accreditation_detail2

from apps. main_accreditation.views import main_accreditations



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name ='index'),
    path('about/', about, name = 'about'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', new_site, name = 'new_site'),
    path('post/<int:id>/', new_post, name='new_post'),
    path('teachers/', teacher_site, name = 'teacher_site'),
    path('teacher/single/<int:id>/', teacher_detail, name = 'teacher_single' ),
    path('classess/',clase, name = 'clase' ),
    path('institutsionaldyk-akkreditatsiya/', accreditations1, name='accreditations1'),    
    path('programmalyk-akkreditatsiya/', accreditations2, name='accreditations2'),
    path('main-akkreditatsiya/', main_accreditations, name='main_accreditations'),
    path('institutsionaldyk-akkreditatsiya_detail/<int:id>/', accreditation_detail1, name = 'accreditations1_detail' ),
    path('programmalyk-akkreditatsiya_detail/<int:id>/', accreditation_detail2, name = 'accreditations2_detail' ),



    

]
urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
