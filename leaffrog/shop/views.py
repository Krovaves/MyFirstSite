from django.contrib.auth.decorators import login_required
from django.db.models import OuterRef, Subquery, Min
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, CreateView

from shop.forms import  AddProductForm, AddProductImgForm, AddProductSpecForm
from shop.models import Goods, Category, GoodsSpecifications, GoodsImages, CategoryImages


class LeafFrogHome(ListView):
    template_name = 'shop/index.html'
    context_object_name = 'post'
    paginate_by = 10
    extra_context = {
        'img': GoodsImages.objects.filter(pk__in=GoodsImages.objects.values('goods_id').annotate(max_pk=Min('pk')).values('max_pk'))
    }

    def get_queryset(self):
        return Goods.published.all()


# class Register(FormView):
#     form_class = Registration
#     template_name = 'shop/register.html'
#     success_url = reverse_lazy('shop')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class Product(DetailView):
    pk_url_kwarg = 'product_id'
    template_name = 'shop/goods/product.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spec'] = GoodsSpecifications.objects.filter(product_id=self.kwargs[self.pk_url_kwarg])
        context['img'] = GoodsImages.objects.filter(goods_id=self.kwargs[self.pk_url_kwarg])
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Goods, pk=self.kwargs[self.pk_url_kwarg])


class Catalog(ListView):
    template_name = 'shop/catalog.html'
    context_object_name = 'cats'
    extra_context = {
        'img': CategoryImages.objects.filter(cat_id__in=Category.objects.all())
    }

    def get_queryset(self):
        return Category.objects.all()


class CatalogSlug(ListView):
    template_name = 'shop/catalog_slug.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['img'] = GoodsImages.objects.filter(pk__in=GoodsImages.objects.values('goods_id').annotate(max_pk=Min('pk')).values('max_pk'))
        return context

    def get_queryset(self):
        return Goods.objects.filter(cat__slug=self.kwargs['cat_slug'])


@login_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        form_img = AddProductImgForm(request.POST, request.FILES)
        form_spec = AddProductSpecForm(request.POST)
        if all([form.is_valid(), form_img.is_valid(), form_spec.is_valid()]):
            goods = form.save()
            images = form_img.save(commit=False)
            images.goods = goods
            images.save()
            GoodsSpecifications.data2(text=form_spec.cleaned_data['text'], id=goods.pk)

            return redirect('shop')
        return render(request, 'shop/add_product.html', {'form': form, 'form_img': form_img, 'form_spec': form_spec})

    else:
        if request.user.seller:
            form = AddProductForm()
            form_img = AddProductImgForm()
            form_spec = AddProductSpecForm()
            return render(request, 'shop/add_product.html', {'form': form, 'form_img': form_img, 'form_spec': form_spec})
    return redirect('shop')


def archive(request, year): # Бесполезная функция, для демонстрации конвертора
    if year > 2024:
        return Http404()
    return HttpResponse(f'<h1>Архив по годам</h><p>{year}</p>')


def page_not_found(request, exception): # Генерирует страницу с 404
    return render(request, 'shop/http404.html')


