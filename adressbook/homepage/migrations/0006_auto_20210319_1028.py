# Generated by Django 3.1.7 on 2021-03-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20210319_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='email'),
        ),
    ]