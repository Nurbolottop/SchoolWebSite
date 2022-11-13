
from django.db import models

# Create your models here.
class Settings(models.Model):
    name_site = models.CharField(
        max_length =255,
        verbose_name ="Мектпетин аты"
        )
    desc2_site = models.CharField(
        max_length =255,
        verbose_name = "Киришуу"
    )
    desc_site =models.TextField(
        verbose_name ="Мектеп боюнча маалымат"
        )
    logo_site = models.ImageField(
        upload_to = 'logo/',
        verbose_name ="Мектептин Суроту"
    )
    slide_site=models.ImageField(
        upload_to = 'slide/',
        verbose_name = "Слайд"
    )
    def __str__(self):
        return self.name_site

    class Meta:
        verbose_name_plural = "Мектеп"
        verbose_name = "Мектеп боюнча"

class Slide(models.Model):
    slide1_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "1-слайд"
    )
    slide2_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "2-слайд"
    )
    slide3_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "3-слайд"
    )
    slide4_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "4-слайд"
    )
    slide5_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "5-слайд"
    )
    slide6_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "6-слайд"
    )
    slide7_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "7-слайд"
    )
    slide8_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "8-слайд"
    )
    slide9_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "9-слайд"
    )
    slide10_site = models.ImageField(
        upload_to ='slides/',
        verbose_name = "10-слайд"
    )




    class Meta:
        verbose_name_plural = "Слайдтар"
        verbose_name = "Слайдтар"

class Lessons(models.Model):
    image = models.ImageField(
        upload_to ='lesson/',
        verbose_name ="Сабактын суроту"
    )
    name = models.CharField(
        max_length =255,
        verbose_name = "Сабактын аты"

    )
    teacher_image =models.ImageField(
        upload_to ='teacher/',
        verbose_name ="Мугалимдин суроту"
    )
    teacher = models.CharField(
        max_length =255,
        verbose_name ="Мугалимдин аты"
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Сабактар"
        verbose_name = "Сабактар"

class Title(models.Model):
    name1 = models.CharField(
        max_length =255,
        verbose_name ="Биринчи Болумдун аты"
    )
    desc1 = models.TextField(
        verbose_name ="Биринчи Болум боюнча маалымат"
    )
    name2 = models.CharField(
        max_length =255,
        verbose_name ="Экинчи Болумдун аты"
    )
    desc2 = models.TextField(
        verbose_name ="Экинчи Болум боюнча маалымат"
    )
    name3 = models.CharField(
        max_length =255,
        verbose_name ="Учунчу Болумдун аты"
    )
    desc3 = models.TextField(
        verbose_name ="Учунчу Болум боюнча маалымат"
    )
    name4 = models.CharField(
        max_length =255,
        verbose_name ="Тортунчу Болумдун аты"
    )
    desc4 = models.TextField(
        verbose_name ="Тортунчу Болум боюнча маалымат"
    )
    def __str__(self):
        return self.name1
    
    class Meta:
        verbose_name_plural ="Болум"
        verbose_name = "Болум"