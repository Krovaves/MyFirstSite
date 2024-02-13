from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from shop.models import Goods, GoodsImages, Category, GoodsSpecifications


# class Registration(forms.ModelForm):
#     GENDER_CHOICES = (
#         ('0', 'Мужской'),
#         ('1', 'Женский'),
#     )
#
#     sex = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label='Пол: ')
#     city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label='Город не выбран', label='Город:')
#     agree = forms.CharField(required=False)
#
#     def clean_agree(self):
#         agree = self.cleaned_data['agree']
#         if not agree:
#             raise ValidationError('Нужно принять соглашение')
#
#     def clean_password(self):
#         password = self.cleaned_data['password']
#         valid_string = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-?!$#@_")
#         if not (set(password) <= set(valid_string)):
#             raise ValidationError("Некорректно введенный пароль.")
#         if len(password) < 6:
#             raise ValidationError("Минимальная длина: 6 символов")
#         return password
#
#     class Meta:
#         model = Users
#         fields = ['first_name', 'last_name', 'sex', 'city', 'password', 'email']
#
#         labels = {
#             'first_name': 'Имя: ',
#             'last_name': 'Фамилия: ',
#             'sex': 'Пол: ',
#             'password': 'Пароль: ',
#             'email': 'Email: '
#         }


class AddProductImgForm(forms.ModelForm):
    class Meta:
        model = GoodsImages
        fields = ['images']


class AddProductForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')

    class Meta:
        model = Goods
        fields = ['title', 'content', 'price', 'cat', 'is_published']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }


class AddProductSpecForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 6}), label='Характеристики')

    class Meta:
        model = GoodsSpecifications
        fields = ['text']








