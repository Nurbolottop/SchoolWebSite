from django.db import models

# Create your models here.
class AcreditationList1(models.Model):
    name = models.CharField(max_length=255, verbose_name='Аты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Институциалдык аккредитация'
        verbose_name_plural = 'Институциалдык аккредитация'

class AcreditationList1Detail(models.Model):
    accreditation = models.ForeignKey(
        AcreditationList1,
        on_delete= models.CASCADE,
        related_name="accreditation",
        verbose_name="Аккредитация"

    )
    accreditation_detail = models.FileField(upload_to='accreditation/', verbose_name='Документ файл')
    name = models.CharField(max_length=255, verbose_name='Аты')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Институциалдык аккредитация болумго киргизуу'
        verbose_name_plural = 'Институциалдык аккредитация болумго киргизуу'
