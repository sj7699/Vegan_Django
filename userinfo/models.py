from django.db import models
from django.conf import settings
class Allergy(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    which_allergy=models.CharField(max_length=100)
    is_category=models.BooleanField(default=False)

class Favor_Category(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    favor_category=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

class Daily_Meal(models.Model):
    meal_id=models.IntegerField(primary_key=True)
    #uid=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    morning = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=True)

class Product(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    amount=models.IntegerField()
    carbohydrate=models.IntegerField()
    sugar=models.IntegerField()
    protein=models.IntegerField()
    fat=models.IntegerField()
    sat_fat=models.IntegerField()
    cholesterol=models.IntegerField()
    product_category=models.CharField(max_length=50)
    price=models.IntegerField()
    product_image=models.ImageField(upload_to="product_image/%Y/%m/%d",default='DEFAULT.jpg')

class MEAL_PRODUCT(models.Model):
    meal_id=models.ForeignKey(Daily_Meal,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)


class Ingredient_Detail(models.Model):
    ingredient_id=models.IntegerField(primary_key=True)
    ingredient_category=models.CharField(max_length=50)

class Product_Ingredient:
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    ingredient_id=models.ForeignKey(Ingredient_Detail,on_delete=models.CASCADE)
    ingredient_name=models.CharField(max_length=100)

class MEAL_PRODUCT(models.Model):
    meal_id=models.ForeignKey(Daily_Meal,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)

# Create your models here.
