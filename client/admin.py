from django.contrib import admin

# Register your models here.
from client.models import Client,Address

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('telegram_id','username','language','phone',)
    search_fields = ('username','name',)
    list_per_page = 10

admin.site.register(Address)