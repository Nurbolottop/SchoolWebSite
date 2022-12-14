# Generated by Django 4.1.1 on 2022-11-18 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acreditationlist2',
            name='file',
        ),
        migrations.CreateModel(
            name='AcreditationList2Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accreditation_detail', models.FileField(upload_to='accreditation/', verbose_name='Документ файл')),
                ('name', models.CharField(max_length=255, verbose_name='Аты')),
                ('accreditation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accreditation', to='accreditation2.acreditationlist2', verbose_name='Аккредитация')),
            ],
            options={
                'verbose_name': 'Программалык аккредитация болумго киргизуу',
                'verbose_name_plural': 'Программалык аккредитация болумго киргизуу',
            },
        ),
    ]
