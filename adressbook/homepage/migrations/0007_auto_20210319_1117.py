# Generated by Django 3.1.7 on 2021-03-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20210319_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='person',
            name='street',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='image'),
        ),
    ]
