# Generated by Django 4.1.2 on 2022-11-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='teacher',
            field=models.CharField(default=1, max_length=255, verbose_name='Мугалимдин аты'),
            preserve_default=False,
        ),
    ]
