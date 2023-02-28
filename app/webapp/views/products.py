from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, render, redirect

from webapp.models import Product

from webapp.forms import ProductForm


def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'detail.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'add.html', context={'form': form})
    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add.html', context={'form': form})
    else:
        Product.objects.create(**form.cleaned_data)
        return redirect('index_page')
