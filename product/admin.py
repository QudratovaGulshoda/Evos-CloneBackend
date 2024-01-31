from django.contrib import admin

# Register your models here.
from product.models import Category,SubCategory,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Category_Picture','title','user')
    list_filter = ('title',)
    list_per_page = 10
    search_fields = ('title',)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','user',)
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 10

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_Picture','title','subcategory','price','discount','updated_at',)
    list_filter = ('title','price','updated_at')
    search_fields = ('title','description')
    list_per_page = 10
