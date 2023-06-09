from django.db import models
from pages.models import Posts


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=50, verbose_name='Прізвище', blank=True)
    email = models.EmailField(verbose_name='E-mail')
    address = models.CharField(max_length=15, verbose_name='Номер телефону')
    # postal_code = models.CharField(max_length=20, verbose_name='Текст внизу')
    city = models.CharField(max_length=100, verbose_name='Адресса')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Posts,on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
