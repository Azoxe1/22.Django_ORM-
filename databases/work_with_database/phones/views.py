from django.shortcuts import render, redirect
from phones.management.commands.import_phones import Command
from django.core.paginator import Paginator

def index(request):
    return redirect('catalog')


def show_catalog(request):
    Command().add_db()
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
