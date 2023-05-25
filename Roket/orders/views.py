from django.shortcuts import render
import requests
from pages.models import Pages
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    t='6105657819:AAE_DdIMVP2MMy0XM30Pvbrnx0PpLm6QAz0'
    c='000000000'
    page = Pages.objects.get(pk=7)
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:

                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            a=request.POST['first_name']
            a1=request.POST['last_name']
            a2=request.POST['email']
            a3=request.POST['address']
            a5=request.POST['city']
            requests.get(f'https://api.telegram.org/bot{t}/sendMessage?chat_id={c}&text=Новый заказ Ім\'я: {a}\n Прізвище: {a1}\nemail: {a2}\nНомер телефону: {a3}\nАдресса: {a5} ')

            return render(request, 'orders/order/created.html',
                          {'order': order,'page':page})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form,'page':page})
