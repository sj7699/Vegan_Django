from datetime import date
from itertools import product
from django.forms import ValidationError
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from userinfo.models import Favor_Category,Product,Daily_Meal
from .serializers import *
from rest_framework import viewsets,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication ,TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
import random
class FavorcategorySet(viewsets.ModelViewSet):
    queryset=Favor_Category.objects.all()
    serializer_class = Favorcategoryserializers
    @action(detail=False)
    def public_list(self, request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['patch'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class Daily_MealSet(viewsets.ReadOnlyModelViewSet):
    queryset=Daily_Meal.objects.all()
    serializer_class = Daily_Mealserializers

class Meal_ProductSet(viewsets.ReadOnlyModelViewSet):
    queryset=MEAL_PRODUCT.objects.all()
    serializer_class = MEAL_PRODUCTserializers

class ProductSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = Productserializers
    @action(detail=False)
    def plist(self,request):
        
        qs=self.queryset
        serializer = self.get_serializer(qs,many=True)
        return Response(serializer.data)

    @action(detail=False)
    def order_by_name(self,request):
        qs=self.queryset.order_by('product_name')
        serializer= self.get_serializer(qs,many=True)
        return Response(serializer.data)  
    
    @action(detail=False)
    def order_by_rname(self,request):
        qs=self.queryset.order_by('-product_name')
        serializer= self.get_serializer(qs,many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def order_by_price(self,request):
        qs=self.queryset.order_by('price')
        serializer= self.get_serializer(qs,many=True)
        return Response(serializer.data)

    @action(detail=False)
    def order_by_rprice(self,request):
        qs=self.queryset.order_by('-price')
        serializer= self.get_serializer(qs,many=True)
        return Response(serializer.data)

class cut_by_price(viewsets.ReadOnlyModelViewSet):
    queryset=Product.objects.all().order_by('?')
    serializer_class=Productserializers
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        print(self.request.user.token)
        price=self.request.query_params.get('price',None)
        rqs=self.queryset.order_by('?')
        print(self.request.user.id)
        if not price.isdigit():
            raise ValidationError("가격은 숫자만")
        price=int(price)
        c=0
        cutcqs=[]
        for x in rqs:
            nowc=x.price
            if(nowc+c>price):
                break
            c+=nowc
            cutcqs.append(x)
        return cutcqs

class meal_by_client(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=Productserializers
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        rqs=[]
        product_list=self.request.data
        for x in product_list:
            meal_list= Daily_Meal.objects.filter(created_at__date=timezone.now().date())
            if(not self.queryset.filter(id=x.id).exists()):
                raise ValidationError("존재하지않는 품목입니다")
            if(x.wtime!="아침" and x.wtime!="점심" and x.wtime!="저녁"):
                raise ValidationError("아침 점심 저녁을 선택해주세요")
            meal_id=1
            if(x.wtime=="아침"):
                if(not meal_list.filter(morning=True).exists()):
                    meal_id=Daily_Meal.objects.create(user=self.request.user,morning=True)
                else:
                    meal_id=meal_list.filter(morning=True)[0]
            if(x.wtime=="점심"):
                if(not meal_list.filter(lunch=True).exists()):
                    meal_id=Daily_Meal.objects.create(user=self.request.user,lunch=True)
                else:
                    meal_id=meal_list.filter(lunch=True)[0]
            if(x.wtime=="저녁"):
                if(not meal_list.filter(dinner=True).exists()):
                    meal_id=Daily_Meal.objects.create(user=self.request.user,dinner=True)
                else:
                    meal_id=meal_list.filter(dinner=True)[0]
            rqs.append(x)
            MEAL_PRODUCT.create(meal_id=meal_id,product_id=x)
        return rqs

class rlist(viewsets.ReadOnlyModelViewSet):
    queryset=Product.objects.all().order_by('?')
    serializer_class=Productserializers
    authentication_classes = [JWTAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        calory=self.request.query_params.get('calory',None)
        rqs=self.queryset.order_by('?')
        if not calory.isdigit():
            raise ValidationError("칼로리는 숫자만")
        wtime=self.request.query_params.get('time',None)
        print(wtime)
        if(wtime is None):
            raise ValidationError("식사할 시간을 입력해주세요 예) 아침 점심 저녁")
        if(wtime!="아침" and wtime!="점심" and wtime!="저녁"):
            raise ValidationError("식사할 시간을 정확히 입력해주세요 예) 아침 점심 저녁")
        calory=float(calory)
        c=0
        cutcqs=[]
        for x in rqs:
            nowc=x.calory
            if(nowc+c>calory):
                break
            c+=nowc
            cutcqs.append(x)
        if(wtime=="아침"):
            mid=Daily_Meal.objects.create(user=self.request.user,morning=True)
            for x in cutcqs:
                MEAL_PRODUCT.objects.create(meal_id=mid,product_id=x)
        if(wtime=="점심"):
            mid=Daily_Meal.objects.create(user=self.request.user,lunch=True)
            for x in cutcqs:
                MEAL_PRODUCT.objects.create(meal_id=mid,product_id=x)
        if(wtime=="점심"):
            mid=Daily_Meal.objects.create(user=self.request.user,dinner=True)
            for x in cutcqs:
                MEAL_PRODUCT.objects.create(meal_id=mid,product_id=x)
        return cutcqs
# Create your views here.
