from django.db import models
from django.conf import settings
from django.utils.timezone import now
import PIL
# Create your models here.

User = settings.AUTH_USER_MODEL

class Room(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    id = models.fields.BigAutoField(primary_key=True)
    title = models.fields.CharField(max_length=100, blank=False, null=False)
    address = models.fields.CharField(max_length=255, blank=False, null=False)
    latitude = models.fields.FloatField(null=True, blank=True)
    longitude = models.fields.FloatField(null=True, blank=True)
    description = models.fields.TextField(null=True, blank=True)
    price = models.fields.FloatField(null=True, blank=True)
    is_parking = models.fields.BooleanField(default=False)
    is_pet = models.fields.BooleanField(default=False)
    is_smoking = models.fields.BooleanField(default=False)
    has_hydro = models.fields.BooleanField(default=False)
    has_aircondition = models.fields.BooleanField(default=False)
    has_water = models.fields.BooleanField(default=False)
    has_heat = models.fields.BooleanField(default=False)
    has_wifi = models.fields.BooleanField(default=False)
    has_tv = models.fields.BooleanField(default=False)
    has_laundry = models.fields.BooleanField(default=False)
    has_fridge = models.fields.BooleanField(default=False)
    has_dishwasher = models.fields.BooleanField(default=False)
    has_dryer = models.fields.BooleanField(default=False)
    has_microwave = models.fields.BooleanField(default=False)
    movein_date = models.fields.DateTimeField(null=True, blank=True)
    created_on = models.fields.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Image(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    default = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = PIL.Image.open(self.image.path)
        output_size = (500,300)
        img.thumbnail(output_size)
        img.save(self.image.path)

    def __str__(self):
        return self.image.name