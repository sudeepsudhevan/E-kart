from django.contrib import admin
from orders.models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "owner",
        "order_status",
        "total_price",
    ]

    search_fields = [
        "owner",
        "id",
    ]


admin.site.register(Order, OrderAdmin)
