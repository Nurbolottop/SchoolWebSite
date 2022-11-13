from django.db import models

# Create your models here.
class New(models.Model):
    language = models.CharField(
        max_length = 244,
        verbose_name ="Сабак"
    )
    name = models.CharField(
        max_length =255,
        verbose_name = "Жанылыктын аты"
    )
    desc =models.TextField(
        verbose_name ="Кошумча маалымат"
    )
    image = models.ImageField(upload_to ='news/', verbose_name ="Жанылыктын суроту")

    created_news = models.DateField(auto_now_add = True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Жанылыктар"
        verbose_name = "Жанылык"    