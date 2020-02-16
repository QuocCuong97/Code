from django.contrib import admin
from .models import Domain, Vendor
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'homepage']
    list_filter = ['name']
    search_fields = ['name']
    fieldsets = [
        ('Tên nhà cung cấp', {'fields': ['name']}),
        ('Trang chủ', {'fields': ['homepage']}),
    ]

class DomainAdmin(admin.ModelAdmin):
    # list_display = ['vendor', 'domain_type', 'origin_price', 'sale_price']
    list_filter = ['domain_type']
    search_fields = ['domain_type']
    fieldsets = [
        ('Nha cung cap', {'fields': ['vendor']}),
        ('Loại tên miền', {'fields': ['domain_type']}),
        ('Giá gốc', {'fields': ['origin_price']}),
        ('Giá khuyến mãi', {'fields': ['sale_price']}),
    ]

admin.site.register(Domain, DomainAdmin)
admin.site.register(Vendor, VendorAdmin)

admin.site.site_header = "Trang quản trị Website"