# Generated by Django 4.1.2 on 2022-11-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_delete_slide'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='desc2_site',
            field=models.CharField(default=1, max_length=255, verbose_name='Киришуу'),
            preserve_default=False,
        ),
    ]
