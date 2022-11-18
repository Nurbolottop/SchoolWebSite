from django.db import models

# Create your models here.
class AcreditationList1(models.Model):
    file = models.FileField(upload_to='acreditation/', verbose_name='Аккредитация файлы')
    name = models.CharField(max_length=255, verbose_name='Аты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Институциалдык аккредитация'
        verbose_name_plural = 'Институциалдык аккредитация'
