# Generated by Django 4.1.2 on 2022-11-10 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_detail',
            name='number',
        ),
        migrations.AddField(
            model_name='contact_detail',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
