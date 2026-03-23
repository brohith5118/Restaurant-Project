from django.contrib import admin
from .models import foodItem,Category,Order,OrderItem

# Register your models here.
admin.site.register(foodItem)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)