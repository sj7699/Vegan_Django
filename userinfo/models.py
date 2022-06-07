from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class User_Detail(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    exercise = models.CharField(max_length=10,default="")
    gender=models.CharField(max_length=20)
    height=models.FloatField()
    weight=models.FloatField()
    vegan_option=models.CharField(max_length=50,default="")
    allergy=models.CharField(max_length=50,default="")
    favor_category=models.CharField(max_length=50,default="")
    avoid_category=models.CharField(max_length=50,default="")


class Daily_Meal(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    morning = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)

class Product(models.Model):
    product_name=models.CharField(max_length=100,default="")
    price=models.IntegerField()
    company=models.CharField(max_length=100,default="") 
    ingredient=models.CharField(max_length=800,default="Nothing")
    amount=models.FloatField()
    serving_size=models.FloatField()
    soduim=models.FloatField()
    carbohydrate=models.FloatField()
    sugar=models.FloatField()
    fat=models.FloatField()
    trans_fat=models.FloatField(default=0.0)
    sat_fat=models.FloatField()
    cholesterol=models.FloatField()
    protein=models.FloatField()
    calory=models.FloatField(default=0)
    vegan_option=models.CharField(max_length=50,default="")
    specific=models.CharField(max_length=100,default="")
    primary_type=models.CharField(max_length=50,default="")
    secondary_type=models.CharField(max_length=50,default="")
    product_category=models.CharField(max_length=50,default="")
    cooking_type=models.CharField(max_length=50,default="")
    product_image=models.ImageField(upload_to="product_image/%Y/%m/%d",default='DEFAULT.jpg')

class MEAL_PRODUCT(models.Model):
    meal_id=models.ForeignKey(Daily_Meal,on_delete=models.CASCADE,related_name='meal',db_column='meal_id')
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product',db_column='product_id')


class Ingredient_Detail(models.Model):
    ingredient_id=models.BigAutoField(primary_key=True)
    ingredient_category=models.CharField(max_length=50)

class Product_Ingredient:
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product',db_column='product_id')
    ingredient_id=models.ForeignKey(Ingredient_Detail,on_delete=models.CASCADE,related_name='Ingredient',db_column='Ingredient_id')
    ingredient_name=models.CharField(max_length=100)

# Create your models here.
