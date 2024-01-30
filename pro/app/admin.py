from django.contrib import admin
# Register your models here.

from .models import Watches
from .models import CartItem
admin.site.register(CartItem)
admin.site.register(Watches)

