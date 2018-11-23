from django.contrib import admin

from .models import Article, Order, Supplier, Detail

# Register your models here.
admin.site.register(Article)
admin.site.register(Order)
admin.site.register(Supplier)
admin.site.register(Detail)