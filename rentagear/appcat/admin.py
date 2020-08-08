from django.contrib import admin

from appcat.models import Gear, OrderGear, Order
from users.models import Profile



admin.site.register(Profile)
admin.site.register (Gear)
admin.site.register (OrderGear)
admin.site.register (Order)