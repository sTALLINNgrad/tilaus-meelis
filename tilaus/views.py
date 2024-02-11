from django.shortcuts import render
from .models import Product

def post_list(request):
    posts = Product.objects.all().values
    return render(request, 'tilaus/index.html', {'posts': posts})