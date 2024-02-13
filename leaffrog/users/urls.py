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
]
