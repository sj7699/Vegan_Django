from rest_framework import serializers
from . models import *

class Favorcategoryserializers(serializers.ModelSerializer):
    class Meta:
        model=Favor_Category
        fields='__all__'

class Allergyserializers(serializers.ModelSerializer):
    class Meta:
        model=Allergy
        fields='__all__'
        
class Daily_Mealserializers(serializers.ModelSerializer):
    class Meta:
        model=Daily_Meal
        fields='__all__'

class Productserializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class MEAL_PRODUCTserializers(serializers.ModelSerializer):
    class Meta:
        model=MEAL_PRODUCT
        fields='__all__'

class Ingredient_Detailserializers(serializers.ModelSerializer):
    class Meta:
        model=Ingredient_Detail
        fields='__all__'

class Product_Ingredientserializers(serializers.ModelSerializer):
    class Meta:
        model=Product_Ingredient
        fields='__all__'
