from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from . models import *
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator   
from rest_framework import viewsets,generics,exceptions,status

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False




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

class Daily_Mealserializers(serializers.ModelSerializer):
    product_name= serializers.CharField(source='product_id.product_name')
    price=serializers.IntegerField(source='product_id.price')
    company=serializers.CharField(source='product_id.company') 
    ingredient=serializers.CharField(source='product_id.ingredient')
    amount=serializers.FloatField(source='product_id.amount')
    serving_size=serializers.FloatField(source='product_id.serving_size')
    sodium=serializers.FloatField(source='product_id.sodium')
    carbohydrate=serializers.FloatField(source='product_id.carbohydrate')
    sugar=serializers.FloatField(source='product_id.sugar')
    fat=serializers.FloatField(source='product_id.fat')
    trans_fat=serializers.FloatField(source='product_id.trans_fat')
    sat_fat=serializers.FloatField(source='product_id.sat_fat')
    cholesterol=serializers.FloatField(source='product_id.cholesterol')
    protein=serializers.FloatField(source='product_id.protein')
    calory=serializers.FloatField(source='product_id.calory')
    vegan_option=serializers.CharField(source='product_id.vegan_option')
    specific=serializers.CharField(source='product_id.specific')
    primary_type=serializers.CharField(source='product_id.primary_type')
    secondary_type=serializers.CharField(source='product_id.secondary_type')
    product_category=serializers.CharField(source='product_id.product_category')
    cooking_type=serializers.CharField(source='product_id.cooking_type')
    product_image=serializers.ImageField(source='product_id.product_image')
    wtime=serializers.SerializerMethodField(source='get_wtime')
    wdate=serializers.SerializerMethodField(source='get_wdate')
    class Meta:
        model=MEAL_PRODUCT
        fields=(
            'product_name','price','wtime','wdate',
            'company','ingredient','amount','serving_size','sodium','carbohydrate',
            'sugar','fat','trans_fat','sat_fat','cholesterol','protein','calory','vegan_option',
            'specific','primary_type','secondary_type','product_category','cooking_type','product_image',
        )
    def get_wtime(self,m):
        if(m.meal_id.morning):
            return "아침"
        if(m.meal_id.lunch):
            return "점심"
        if(m.meal_id.dinner):
            return "저녁"
        return "저녁"
    def get_wdate(self,m):
        return m.meal_id.created_at.date()
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
    def validate_exercise(self,instance):
        if(instance!="low" and instance!="middle" and instance!="high"):
            raise exceptions.ParseError("exercise shoudld be low middle high")
        return instance
    def validate_height(self,instance):
        if(not isfloat(instance)):
            raise exceptions.ParseError("키는 숫자여야만합니다")
        return instance
    def validate_weight(self,instance):
        if(not isfloat(instance)):
            raise exceptions.ParseError("체중은 숫자여야만합니다")
        return instance
