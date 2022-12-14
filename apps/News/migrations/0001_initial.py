# Generated by Django 4.1.2 on 2022-11-05 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=244, verbose_name='Сабак')),
                ('name', models.CharField(max_length=255, verbose_name='Жанылыктын аты')),
                ('desc', models.TextField(verbose_name='Кошумча маалымат')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Жанылыктын суроту')),
                ('created_news', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Жанылык',
                'verbose_name_plural': 'Жанылыктар',
            },
        ),
    ]
