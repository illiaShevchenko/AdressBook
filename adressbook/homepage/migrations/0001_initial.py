# Generated by Django 3.1.7 on 2021-03-16 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=15, verbose_name='Имя')),
                ('patronym', models.CharField(max_length=15, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон')),
            ],
        ),
    ]
