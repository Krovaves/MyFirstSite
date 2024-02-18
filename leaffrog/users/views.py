from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, CreateView, DetailView, UpdateView

from leaffrog import settings
from users.forms import LoginUserForm, RegistrationForm, ProfileEditForm, UserPasswordChangeForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    # def get_success_url(self):
    #     return reverse_lazy('shop')


# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('shop'))
#     else:
#         form = LoginUserForm()
#
#     return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def favourites(request):
    return HttpResponseRedirect(reverse('shop'))


def cart(request):
    return HttpResponseRedirect(reverse('shop'))


def profile(request):
    return HttpResponseRedirect(reverse('shop'))


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('shop')


class ProfileUser(LoginRequiredMixin, DetailView):
    template_name = 'users/profile.html'
    context_object_name = 'profile_data'
    extra_context = {
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        if user.seller is True:
            context['menu'] = [
                {'title': 'Добавить товар', 'url_name': 'add_product'},
                {'title': 'Мои товары', 'url_name': 'users:cart'},
                {'title': 'Избранное', 'url_name': 'users:login'},
                {'title': 'Заказы', 'url_name': 'catalog'},
                {'title': 'Изменить', 'url_name': 'users:profile_edit'},
                {'title': 'Выйти', 'url_name': 'users:logout'},
            ]
        else:
            context['menu'] = [
                {'title': 'Главная', 'url_name': 'shop'},
                {'title': 'Избранное', 'url_name': 'users:login'},
                {'title': 'Заказы', 'url_name': 'catalog'},
                {'title': 'Изменить', 'url_name': 'users:profile_edit'},
                {'title': 'Выйти', 'url_name': 'users:logout'},
            ]

        context['data'] = [
                {'title': 'Логин', 'value': user.username},
                {'title': 'Имя', 'value': user.first_name},
                {'title': 'Фамилия', 'value': user.last_name},
                {'title': 'Email', 'value': user.email},
                {'title': 'Город', 'value': user.city},
                {'title': 'Статус', 'value': user.seller},
            ]

        return context


class ProfileEditUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileEditForm
    template_name = 'users/profile_edit.html'
    extra_context = {
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        if user.seller is True:
            context['menu'] = [
                {'title': 'Добавить товар', 'url_name': 'add_product'},
                {'title': 'Мои товары', 'url_name': 'users:cart'},
                {'title': 'Избранное', 'url_name': 'users:login'},
                {'title': 'Заказы', 'url_name': 'catalog'},
                {'title': 'Изменить', 'url_name': 'users:profile_edit'},
                {'title': 'Выйти', 'url_name': 'users:logout'},

            ]
        else:
            context['menu'] = [
                {'title': 'Главная', 'url_name': 'shop'},
                {'title': 'Избранное', 'url_name': 'users:login'},
                {'title': 'Заказы', 'url_name': 'catalog'},
                {'title': 'Изменить', 'url_name': 'users:profile_edit'},
                {'title': 'Выйти', 'url_name': 'users:logout'},
            ]

        context['data'] = [
                {'title': 'Логин', 'value': user.username},
                {'title': 'Имя', 'value': user.first_name},
                {'title': 'Фамилия', 'value': user.last_name},
                {'title': 'Email', 'value': user.email},
                {'title': 'Город', 'value': user.city},
                {'title': 'Статус', 'value': user.seller},
            ]

        return context


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
