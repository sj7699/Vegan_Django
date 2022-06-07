from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from . models import *
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator   
class Daily_Mealserializers(serializers.ModelSerializer):
    class Meta:
        model=Daily_Meal
        fields='__all__'

class Productserializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
    def validate_product_name(self,instance):
        if(len(instance)<2):
            raise serializers.ValidationError(detail="상품이름이 너무 짧습니다")
        return instance
    
    def validate_price(self,instance):
        if(instance<=0):
            raise serializers.ValidationError(detail="가격이 너무 낮습니다.")
        return instance

    def validate_product_category(self,instance):
        if(len(instance)<1):
            raise serializers.ValidationError(detail="카테고리를 입력해주세요.")
        return instance

    def validate_amount(self,instance):
        if(instance<1):
            raise serializers.ValidationError(detail="용량이 너무 낮습니다")
        return instance

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

class User_Detailserializers(serializers.ModelSerializer):
    class Meta:
        model=User_Detail
        fields='__all__'