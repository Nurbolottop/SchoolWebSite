from django.contrib import admin
from apps.settings.models import  Settings, Slide,Title
# Register your models here.
admin.site.register(Settings)
admin.site.register(Slide)
admin.site.register(Title)