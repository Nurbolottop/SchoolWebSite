
from django.db import models

# Create your models here.
class Contact(models.Model):
    call =models.CharField(
        max_length =255,
        verbose_name = "Телефонный номер"
    )
    email = models.EmailField(
        verbose_name = "Почта"
    )
    location = models.CharField(
        max_length =255,
        verbose_name = "Адрес"
    )
    facebook_site = models.URLField(
        verbose_name = "Facebook ссылка"
    )
    instagram_site = models.URLField(
        verbose_name = "Instagram ccылка"
    )
    youtube_site = models.URLField(
        verbose_name = "Ютуб ссылка"
    )
    work_site = models.CharField(
        max_length = 255,
        verbose_name = "Иш кундору"
    )
    work2_site = models.CharField(
        max_length = 255,
        verbose_name = "Иш сааттары!"
    )
    def __str__(self):
        return self.call

    class Meta:
        verbose_name_plural = "Контакттар"
        verbose_name = "Контакттар"

class Contact_detail(models.Model):
    name =models.CharField(max_length =255)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return f"{self.name} {self.message}"

    class Meta:
        verbose_name_plural = "Акыркы байланыштар"
        verbose_name = "Акыркы байланыштар"  