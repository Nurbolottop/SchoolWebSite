# Generated by Django 4.1.2 on 2022-11-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='title',
            name='name',
        ),
        migrations.AddField(
            model_name='title',
            name='desc1',
            field=models.TextField(default=1, verbose_name='Биринчи Болум боюнча маалымат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='desc2',
            field=models.TextField(default=1, verbose_name='Экинчи Болум боюнча маалымат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='desc3',
            field=models.TextField(default=1, verbose_name='Учунчу Болум боюнча маалымат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='desc4',
            field=models.TextField(default=1, verbose_name='Тортунчу Болум боюнча маалымат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='name1',
            field=models.CharField(default=1, max_length=255, verbose_name='Биринчи Болумдун аты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='name2',
            field=models.CharField(default=1, max_length=255, verbose_name='Экинчи Болумдун аты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='name3',
            field=models.CharField(default=1, max_length=255, verbose_name='Учунчу Болумдун аты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='name4',
            field=models.CharField(default=1, max_length=255, verbose_name='Тортунчу Болумдун аты'),
            preserve_default=False,
        ),
    ]
