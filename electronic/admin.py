from django.contrib import admin

from electronic.models import Contact, Product, Supplier, NetWork


@admin.action(description='Обнулить задолженность перед поставщиком')
def debt_to_supplier_reset(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('city', 'country')
    list_filter = ('city', 'country',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'level',)
    list_filter = ('level',)


@admin.register(NetWork)
class NetWorkAdmin(admin.ModelAdmin):

    list_display = ('name', 'contact', 'product', 'supplier', 'debt_to_supplier', 'created_at')
    list_display_links = ('name', 'supplier',)
    list_filter = ('contact__city', 'contact__country', 'supplier__level',)
    search_fields = ('contact__city', 'contact__country', 'supplier__level',)
    actions = (debt_to_supplier_reset,)
