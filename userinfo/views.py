from django.forms import ValidationError
from django.shortcuts import render
from django.contrib.auth.models import User
from userinfo.models import Favor_Category,Product
from .serializers import *
from rest_framework import viewsets,generics
from rest_framework.decorators import action
from rest_framework.response import Response
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

class rlist(viewsets.ReadOnlyModelViewSet):
    queryset=Product.objects.all().order_by('?')
    serializer_class=Productserializers
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
            mid=Daily_Meal.objects.create(user=self.request.user.id,morning=True)
            for x in cutcqs:
                MEAL_PRODUCT.objects.create(meal_id=mid,product_id=x)
        if(wtime=="점심"):
            mid=Daily_Meal.objects.create(user=self.request.user.id,lunch=True)
            for x in cutcqs:
                MEAL_PRODUCT.objects.create(meal_id=mid,product_id=x)
        if(wtime=="점심"):
            mid=Daily_Meal.objects.create(user=self.request.user.id,dinner=True)
            for x in cutcqs:
                MEAL_PRODUCT.objects.create(meal_id=mid,product_id=x)
        return cutcqs



# Create your views here.
