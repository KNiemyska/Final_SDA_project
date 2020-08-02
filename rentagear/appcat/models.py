import uuid
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(blank=True, null=True)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title




class Gear(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    title=models.CharField(max_length=250, blank=False, null=False)
    year_of_production=models.CharField(max_length=4)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    picture=models.ImageField(upload_to='gear_pics', default="default_gear.jpg")

    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # gear_status=models.ForeignKey(GearStatus, models.SET_NULL)
    def __str__(self):
        return self.title
    #redirect will redirect to a specific route
    #reverse will return full url to that route as a string
    #in this case we want to return url as a string and let the view handle redirect for us:
    #first import reverse function
    def get_absolute_url(self): #django has to know how to find absolut location of gear -> we want django to redirect to gear detail_form
        return reverse('gear-detail',kwargs={'pk':self.pk})


class GearStatus(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    gs_name=models.CharField(max_length=20)

class GearCopy(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    gc_gear_id=models.ForeignKey(Gear,on_delete=models.CASCADE)
    # gc_status_id=models.ForeignKey(GearStatus, on_delete=models.CASCADE)

# class Item (models.Model):
#     title= models.Charfield(max_length=100)
#     def __str__(self):
#         return self.title
#
# class OrderItem(models.Model):
#     item=models.ForeignKey(Item, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.title
#
# class Order(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     items=models.ManyToManyRel(OrderItem)
#     start_date=models.DateTimeField(auto_now_add=True)
#     ordered_date=models.DateTimeField()
#     ordered= models.BooleanField(default=False)
#     def __str__(self):
#         return self.title

