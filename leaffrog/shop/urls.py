from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitConverter, 'year4')

urlpatterns = [
    path('', views.LeafFrogHome.as_view(), name='shop'),
    path('archive/<year4:year>/', views.archive), # бесполезный путь для демонстрации конвертора
    #path('registering/', views.Register.as_view(), name='reg'),
    path('product/<int:product_id>/', views.Product.as_view(), name='product'),
    path('catalog/<slug:cat_slug>/', views.CatalogSlug.as_view(), name='catalog_slug'),
    path('catalog/', views.Catalog.as_view(), name='catalog'),
    path('add_product/', views.add_product, name='add_product'),

]