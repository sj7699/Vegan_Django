from django.db import models
from django.conf import settings
class Allergy(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    which_allergy=models.CharField(max_length=100)

class Favor_Category(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    favor_category=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

# Create your models here.
