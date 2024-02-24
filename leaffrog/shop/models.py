from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.urls import reverse
from transliterate import slugify
import re





class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class Goods(models.Model):
    class Status(models.IntegerChoices):
        HIDDEN = 0, 'Скрыт'
        PUBLISHED = 1, 'Опубликован'

    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=True, verbose_name='Статус')
    cat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='goods',
                            verbose_name='Категория')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})


class GoodsSpecifications(models.Model):
    parameter = models.CharField(max_length=255)
    value = models.CharField(max_length=255, null=True, default='', blank=True)
    product = models.ForeignKey('Goods', on_delete=models.CASCADE, related_name='specific')

    def __str__(self):
        return f'{self.parameter} : {self.value}'

    @classmethod
    def data(cls, data_str, id):
        #id = 15
        #data_str = """
#Размер экрана: 55"(139 см)
#Технология экрана: DLED
#Разрешение экрана: UHD 4K (3840x2160)
#Частота обновления экрана, в Гц: 60Hz
#Голосовой помощник: Салют
#Прием ТВ сигнала: Цифровое ТВ (DVB-T2)
#Беспроводное подключение: Bluetooth/Wi-Fi
#Мощность звука, в Вт: 20
#Разъемы: Optical; RJ-45 (LAN/Ethernet); Модуль CI+
#Количество HDMI: 3
#Количество USB: 2
#Размер настенного крепления VESA: 200x200
#Габариты без подставки, см (ВxШxГ): 71,4x123,6x7,7
#Габариты с подставкой, см (ВxШxГ): 76,9x123,6x25,2
#        """

        # Используем регулярное выражение для разбиения на пары значений
        pairs = re.findall(r'(.+?)\n(.+)', data_str)

        # Преобразуем пары значений в список списков
        result = [[pair[0], pair[1]] for pair in pairs]
        for i in result:
            print(i[0])
            print(i[1])
            GoodsSpecifications.objects.create(parameter=i[0].strip(), value=i[1].strip(), product_id=id)

    @classmethod
    def data2(cls, text, id):
        # id = 15
        # data_str = """
        # Размер экрана: 55"(139 см)
        # Технология экрана: DLED
        # Разрешение экрана: UHD 4K (3840x2160)
        # Частота обновления экрана, в Гц: 60Hz
        # Голосовой помощник: Салют
        # Прием ТВ сигнала: Цифровое ТВ (DVB-T2)
        # Беспроводное подключение: Bluetooth/Wi-Fi
        # Мощность звука, в Вт: 20
        # Разъемы: Optical; RJ-45 (LAN/Ethernet); Модуль CI+
        # Количество HDMI: 3
        # Количество USB: 2
        # Размер настенного крепления VESA: 200x200
        # Габариты без подставки, см (ВxШxГ): 71,4x123,6x7,7
        # Габариты с подставкой, см (ВxШxГ): 76,9x123,6x25,2
        #        """

        pairs = [pair.strip().split(':') for pair in text.split('\n') if pair]
        data_dict = {pair[0]: pair[1] for pair in pairs}
        for key, value in data_dict.items():
            GoodsSpecifications.objects.create(parameter=key, value=value, product_id=id)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default='')

     # from transliterate import slugify
     #for w in Category.objects.all():
     #    w.slug = slugify(w.name)
     #    w.save(update_fields=("slug",))

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_slug', kwargs={'cat_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class GoodsImages(models.Model):
    images = models.ImageField(upload_to='img_goods/%Y/%m/%d', default=None, null=True, blank=True,
                            verbose_name='Изображение')
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE, related_name='img')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class CategoryImages(models.Model):
    images = models.ImageField(upload_to='img_cat/%Y/%m/%d', default=None, null=True, blank=True,
                            verbose_name='Изображение')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='img')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
