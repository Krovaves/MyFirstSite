from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, CreateView, DetailView

from users.forms import LoginUserForm, RegistrationForm


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

    def get_object(self, queryset=None):
        return self.request.user
