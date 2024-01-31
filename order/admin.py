from django.contrib import admin

# Register your models here.
from order.models import Order,OrderItem

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','quantity','cost',)
    list_per_page = 10

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('all_items','all_cost','user',)
    search_fields = ('all_items',)
    list_per_page = 10