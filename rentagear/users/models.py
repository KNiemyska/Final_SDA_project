import uuid

from django.db import models
from django.contrib.auth.models import User

from appcat.models import GearCopy
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self): #override save methods to add some functionaly - change photos to smaller
        super().save()
        img=Image.open(self.image.path)
        if img.height > 300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class UserTable(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user_name=models.CharField(max_length=15, blank=False, null=False)
    user_surname=models.CharField(max_length=50, blank=False, null=False)
    user_email=models.CharField(max_length=100, blank=False, null=False)
    user_phone=models.CharField(max_length=9, blank=False, null=False)




class UserGearRent(models.Model):

    id=models.ForeignKey(GearCopy, on_delete=models.CASCADE)
    ug_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    ug_rent_date=models.DateField()
    ug_return_date=models.DateField()
    ug_user_id=models.ForeignKey(UserTable, on_delete=models.CASCADE)