from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from cart.cart import Cart
from django.http import HttpResponseRedirect
from django.contrib import messages
# from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
# from cloudipsp import Api, Checkout


def base(request):
    cart = Cart(request)
    page = Pages.objects.get(pk=1)
    return render(request, 'pages/main.html', {'page':page,'cart': cart})

def main(request):
    cart = Cart(request)
    # counter = Counter.objects.all()
    page = Pages.objects.get(pk=1)
    category = Category.objects.all()
    posts = Posts.objects.all()[0:3]
    slider = Slider.objects.all()
        
    return render(request, 'pages/index.html', {'page':page , 'posts':posts ,'cart': cart, 'category':category , 'slider':slider})


def products(request , post_categoryid):
    cart = Cart(request)
    
    page = Pages.objects.get(pk=2)
    posts = Posts.objects.filter(categoryid=post_categoryid)
    category = Category.objects.filter(id=post_categoryid)

    return render(request, 'pages/products.html', {'page':page,'posts':posts ,'cart': cart,'category':category})

def dostavka(request):
    cart = Cart(request)
    page = Pages.objects.get(pk=3)
    form = SubscribeForm(request.POST )
   
    if request.method == 'POST' and form.is_valid():
        new_form=form.save()
        messages.error(request,'Ваше сообщение отправленно')
        return HttpResponseRedirect('#top')
    return render(request, 'pages/dostavka.html', {'page':page,'form': form,'cart': cart})

def view_posts(request, post_id):
    cart = Cart(request)
    page = Pages.objects.get(pk=4)
    post_item = get_object_or_404(Posts, pk=post_id)
    posts = Posts.objects.all()[0:5]
    category = Category.objects.all()
    photos = Photos.objects.filter(title=post_id)

    return render(request, 'pages/single-post.html', {"post_item": post_item ,'cart': cart, 'page':page , 'posts':posts , 'category':category , 'photos':photos})


def contacts(request):
    cart = Cart(request)
    page = Pages.objects.get(pk=5)
    return render(request, 'pages/contact-us.html', {'page':page,'cart': cart})

def category(request):
    cart = Cart(request)
    search = request.GET.get('search' , '')
    if search:
        products = Posts.objects.filter(title__contains=search)
    else:
        products = None

    page = Pages.objects.get(pk=6)
    category = Category.objects.all()
    return render(request, 'pages/products-category.html', {'page':page , 'category':category,'cart': cart,'search':search, 'products':products})#,'search':search, 'products':products

def error404(request,exeption):
    cart = Cart(request)
    return render(request,'pages/404.html')

def error500(request):
    cart = Cart(request)
    return render(request,'pages/404.html')






