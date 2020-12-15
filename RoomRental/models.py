from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Room(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.SET_NULL, null=True)
    id = models.fields.BigAutoField(primary_key=True)
    title = models.fields.CharField(max_length=100, blank=False, null=False)
    content = models.fields.TextField()
    created_on = models.fields.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title