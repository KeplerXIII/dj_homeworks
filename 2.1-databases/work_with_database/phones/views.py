from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort', 'name')
    if sort_type == 'min_price':
        sort_type = 'price'
    if sort_type == 'max_price':
        sort_type = '-price'
    phone_objects = Phone.objects.order_by(sort_type).all()
    phone_list = [x for x in phone_objects]
    context = {
        'phones': phone_list
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)
