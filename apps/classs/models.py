from django.db import models

# Create your models here.
class Classe(models.Model):
    image = models.ImageField(upload_to = 'class/', verbose_name = "Класстын суроту")

    name = models.CharField(max_length =255, verbose_name = "Класстын аты")

    prod = models.CharField(max_length =244, verbose_name = "Класстын жумалык графиги")
    
    prod1 = models.CharField(max_length =244, verbose_name = "Класстын кунумдук графиги")


    teacher = models.CharField(max_length =255, verbose_name = "Класс жетекчиси")

    teacher_image = models.ImageField(upload_to = 'class_teacher/', verbose_name = "Класс жетекчинин суроту")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Класстар"
        verbose_name = "Класстар"