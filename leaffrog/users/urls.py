from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('favourites/', views.favourites, name='favourites'),
    path('registering/', views.RegisterUser.as_view(), name='reg'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditUser.as_view(), name='profile_edit'),
    path('profile/edit/password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('profile/edit/password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]
