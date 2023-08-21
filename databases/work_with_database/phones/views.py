from django.shortcuts import render, redirect
from phones.management.commands.import_phones import Command
from django.core.paginator import Paginator
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    one_phones = Phone.objects.get(slug = slug)
    context = {'phone':one_phones}
    return render(request, template, context)

