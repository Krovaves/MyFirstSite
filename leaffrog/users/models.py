from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from transliterate import slugify

from shop.models import Goods


class User(AbstractUser):
    class Sex(models.IntegerChoices):
        MALE = 0, 'Мужской'
        FEMALE = 1, 'Женский'

    class Seller(models.IntegerChoices):
        USER = 0, 'Пользователь'
        SELLER = 1, 'Продавец'

    sex = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Sex.choices)),
                                       default=True, verbose_name='Пол')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, related_name='user', verbose_name='Город')
    seller = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Seller.choices)), default=False,
                                 blank=True)
    orders = models.ManyToManyField(Goods, blank=True, related_name='orders')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, verbose_name='Фотография')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class City(models.Model):
    city = models.CharField(max_length=255, db_index=True, verbose_name='Город')
    slug = models.SlugField(max_length=255, blank=True, verbose_name='Слаг')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.city)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
