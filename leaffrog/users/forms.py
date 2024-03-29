from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError

from users.models import City, User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(), label='Логин или Email', min_length=3)
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль', min_length=4)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    GENDER_CHOICES = (
        ('0', 'Мужской'),
        ('1', 'Женский'),
    )

    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите', widget=forms.PasswordInput())
    sex = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label='Пол: ')
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label='Город не выбран', label='Город:')
    agree = forms.CharField(required=False)

    def clean_agree(self):
        agree = self.cleaned_data['agree']
        if not agree:
            raise ValidationError('Нужно принять соглашение')

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой Email уже существует')
        return email

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if get_user_model().objects.filter(username=username).exists():
    #         raise forms.ValidationError('Такой Логин уже существует')
    #     return username

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'sex', 'city', 'password1', 'password2', 'email']

        labels = {
            'first_name': 'Имя: ',
            'last_name': 'Фамилия: ',
            'sex': 'Пол: ',
            'password': 'Пароль: ',
            'email': 'Email: '
        }


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(), min_length=3, required=False, disabled=True)
    email = forms.CharField(label='Email', widget=forms.EmailInput(), required=False, disabled=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'photo']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput()
        }

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if email and get_user_model().objects.filter(email=email).exists():
    #         raise forms.ValidationError('Такой Email уже существует')
    #     return email
    #
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if username and get_user_model().objects.filter(username=username).exists():
    #         raise forms.ValidationError('Такой Логин уже существует')
    #     return username


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
