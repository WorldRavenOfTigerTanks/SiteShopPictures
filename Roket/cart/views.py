from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pages.models import Posts
from pages.models import Pages
from .cart import Cart
from .forms import CartAddProductForm



@require_POST
def cart_add(request, post_id):
    cart = Cart(request)
    product = get_object_or_404(Posts, id=post_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, post_id):
    cart = Cart(request)
    product = get_object_or_404(Posts, id=post_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    page = Pages.objects.get(pk=7)
    return render(request, 'cart/detail.html', {'cart': cart,'page':page})