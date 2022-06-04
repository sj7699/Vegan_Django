from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from . models import *
from rest_framework.authtoken.models import Token
from rest_framwork.validators import UniqueValidator
class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2=serializers.CharField(write_only=True,required=True)
    class Meta:
        model = User
        fields = ('username','pssword','password2','email')
    def vaildate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password":"Password fields didn't match"}
            )
        return data
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
