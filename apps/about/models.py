from django.db import models

# Create your models here.
class About(models.Model):
    slide1 = models.ImageField(upload_to = 'about_slide/',verbose_name='Биринчми сурот')
    slide2= models.ImageField(upload_to = 'about_slide/',verbose_name="Экинчи сурот")   
    desc = models.TextField(verbose_name= "Биздин миссия боюнча кошумча маалымат!")
    talap1 = models.CharField(max_length=255, verbose_name='Биринчи талап')
    talap2 = models.CharField(max_length=255, verbose_name='Экинчи талап')
    talap3 = models.CharField(max_length=255, verbose_name='Учунчу талап')

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = 'Биз жонундо'
        verbose_name_plural = 'Биз жонундо'