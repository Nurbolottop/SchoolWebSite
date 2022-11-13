# Generated by Django 4.1.2 on 2022-11-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call', models.CharField(max_length=255, verbose_name='Телефонный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('location', models.CharField(max_length=255, verbose_name='Адрес')),
                ('facebook_site', models.URLField(verbose_name='Facebook ссылка')),
                ('instagram_site', models.URLField(verbose_name='Instagram ccылка')),
                ('youtube_site', models.URLField(verbose_name='Ютуб ссылка')),
                ('work_site', models.CharField(max_length=255, verbose_name='Иш кундору')),
                ('work2_site', models.CharField(max_length=255, verbose_name='Иш сааттары!')),
            ],
            options={
                'verbose_name': 'Контакттар',
                'verbose_name_plural': 'Контакттар',
            },
        ),
    ]
