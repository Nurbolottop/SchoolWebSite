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
from apps.settings.views import about, index
from apps.News.views import new_site,new_post
from apps.contact.views import contacts
from apps.teachers.views import teacher_site,teacher_detail
from apps.classs.views import clase
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name ='index'),
    path('about/', about, name = 'about'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', new_site, name = 'new_site'),
    path('post/<int:id>/', new_post, name='new_post'),
    path('teachers/', teacher_site, name = 'teacher_site'),
    path('teacher/single/<int:id>/', teacher_detail, name = 'teacher_single' ),
    path('classess/',clase, name = 'clase' )

]
urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
