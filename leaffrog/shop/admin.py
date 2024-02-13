from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Goods, Category,  GoodsImages


# @admin.register(Goods)
# class GoodsAdmin(admin.ModelAdmin):
#     #fields = ('title',  'price', 'cat')
#     list_display = ('id', 'title', 'goods_img', 'price', 'cat', 'description_length', 'time_update', 'is_published')
#     list_display_links = ('id', 'title')
#     ordering = ['id']
#     #readonly_fields = ['goods_img']
#     list_editable = ('is_published',)
#     list_per_page = 10
#     actions = ['set_published', 'set_hidden']
#     search_fields = ['title']
#     list_filter = ['cat__name', 'is_published']
#
#     @admin.display(description='Описание')
#     def description_length(self, description: Goods):
#         return f'Количество символов описания: {len(description.content)}'
#
#     @admin.action(description='Опубликовать товары')
#     def set_published(self, request, queryset):
#         count = queryset.update(is_published=Goods.Status.PUBLISHED)
#         self.message_user(request, f'Опубликовано товаров: {count}')
#
#     @admin.action(description='Скрыть товары')
#     def set_hidden(self, request, queryset):
#         count = queryset.update(is_published=Goods.Status.HIDDEN)
#         self.message_user(request, f'Скрыто товаров: {count}', messages.WARNING)
#
#     @admin.display(description='Изображение')
#     def goods_img(self, obj):
#         images = obj.img.all()
#         if images:
#             return mark_safe(f"<img src='{images[0].images.url}' width=50>")
#         return "Нет изображения"
#
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     list_display_links = ('id', 'name')
#     prepopulated_fields = {'slug': ('name', )}


# @admin.register(Users)
# class UsersAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'seller', 'sex', 'city', 'password', 'email', 'time_update',
#                     'time_create')
#     list_display_links = ('id', 'first_name', 'last_name')
#     ordering = ['id']
#     list_editable = ('seller',)
#     list_per_page = 10
#     search_fields = []
#     list_filter = ['city', 'seller']
#
#
# @admin.register(City)
# class CityAdmin(admin.ModelAdmin):
#     list_display = ('id', 'city', 'slug')
#     list_display_links = ('id', 'city')
#     prepopulated_fields = {'slug': ('city', )}
# # admin.site.register(Goods, GoodsAdmin)
