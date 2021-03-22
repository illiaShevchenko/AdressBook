from django.db import models


class Person(models.Model):
    surname = models.CharField('surname', max_length = 30)
    name = models.CharField('name', max_length = 15)
    phone = models.CharField('phone', max_length = 10)
    email = models.EmailField('email', max_length = 50, null = True, blank = True)
    image = models.ImageField('image', upload_to='person_images/', default= '../static/homepage/images/Icon-user.png')
    country = models.CharField('Страна', max_length = 20, null = True, blank = True)
    city = models.CharField('Город', max_length = 20, null = True, blank = True)
    street = models.CharField('Улица', max_length = 20, null = True, blank = True)

    def __str__(self):
        return self.surname

    class Meta:
        unique_together = ('surname', 'name')
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
