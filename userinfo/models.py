from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Allergy(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    which_allergy=models.CharField(max_length=100)
    is_category=models.BooleanField(default=False)

class Favor_Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    is_public = models.BooleanField(default=False)
    favor_category=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

class Daily_Meal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    morning = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=True)

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    company=models.CharField(max_length=100,default="")
    amount=models.IntegerField()
    calory=models.IntegerField(default=0)
    carbohydrate=models.IntegerField()
    sugar=models.IntegerField()
    protein=models.IntegerField()
    fat=models.IntegerField()
    sat_fat=models.IntegerField()
    trans_fat=models.IntegerField(default=0)
    cholesterol=models.IntegerField()
    product_category=models.CharField(max_length=50,default="")
    price=models.IntegerField()
    soduim=models.IntegerField(default=0)
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
