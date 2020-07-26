from django.contrib import admin

from appcat.models import Gear
from users.models import Profile



admin.site.register(Profile)
admin.site.register (Gear)
