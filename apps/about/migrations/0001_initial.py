# Generated by Django 4.1.2 on 2022-11-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide1', models.ImageField(upload_to='about_slide/', verbose_name='Биринчми сурот')),
                ('slide2', models.ImageField(upload_to='about_slide/', verbose_name='Экинчи сурот')),
                ('desc', models.TextField(verbose_name='Биздин миссия боюнча кошумча маалымат!')),
                ('talap1', models.CharField(max_length=255, verbose_name='Биринчи талап')),
                ('talap2', models.CharField(max_length=255, verbose_name='Экинчи талап')),
                ('talap3', models.CharField(max_length=255, verbose_name='Учунчу талап')),
            ],
        ),
    ]
