from django.db import models
from django.db.models.signals import post_save
from django.dispatch import Signal
# Create your models here.
from product.models import Product
from client.models import Client

class Order(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE,to_field='telegram_id')

    @property
    def user(self):
        return self.client.name


    @property
    def all_cost(self):
        items = self.items.all()
        total = sum([item.cost for item in items])
        return total


    @property
    def all_items(self):
        items = self.items.all()
        total = sum([item.quantity for item in items])
        return total

    def __str__(self):
        return f"{self.client.telegram_id} IDli foydalanuvchi"


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    @property
    def cost(self):
        total = self.quantity * (self.product.price-self.product.discount)
        return total

    def __str__(self):
        return "Buyurtma"

def create_order(sender,instance,created,**kwargs):
    if created:
        Order.objects.create(
            client=instance
        )
Signal.connect(post_save,create_order,sender=Client)