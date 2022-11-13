from django.db import models

# Create your models here.
class Teacher(models.Model):
    image = models.ImageField(
        upload_to = 'teacher/',
        verbose_name = "Мугалимдин суроту"
    )
    desc = models.TextField(verbose_name ="Мугалим жонундо маалымат")
    name = models.CharField(
        max_length =255,
        verbose_name ="Мугалимдин аты-жону"
    )
    work = models.CharField(
        max_length =255,
        verbose_name ="Мугалимдин иши"
    )
    year = models.CharField(max_length =255, verbose_name ="Мугалимдин туулган жылы")

    edu = models.TextField(verbose_name ="Мугалимдин окуган жери")

    oput = models.CharField(max_length =255, verbose_name ="Мугалимдин тажрыйбасы")


    number = models.CharField(
        max_length =255,
        verbose_name = "Мугалимдин номери"
    )
    email = models.CharField(max_length =255, verbose_name ="Мугалимдин почтасы")

    facebook = models.URLField(
        verbose_name = "Мугалимдин Facebook баракчасы"
    )
    instagram  =models.URLField(
        verbose_name ="Мугалимдин Instagram баракчасы"
    )
    whatsapp = models.URLField(
        verbose_name = "Мугалимдин WhatsApp баракчасы"
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Мугалимдер"
        verbose_name = "Мугалимдер"