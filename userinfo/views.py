from datetime import date
from itertools import product
from django.forms import ValidationError
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from userinfo.models import Favor_Category,Product,Daily_Meal
from .serializers import *
from django.db.models import Q
from rest_framework import viewsets,generics,exceptions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication ,TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
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
        qparam_price_low_range=request.query_params.get("price_low")
        if(qparam_price_low_range is not None):
            if(not qparam_price_low_range.isdigit()):
                raise exceptions.ParseError("가격범위는 숫자만")
            qparam_price_low_range=int(qparam_price_low_range)
            qs=qs.filter(price__gte=qparam_price_low_range)
        qparam_price_high_range=request.query_params.get("price_high")
        if(qparam_price_high_range is not None):
            if(not qparam_price_high_range.isdigit()):
                raise exceptions.ParseError("가격범위는 숫자만")
            qparam_price_high_range=int(qparam_price_high_range)
            qs=qs.filter(price__lte=qparam_price_high_range)
        qparam_price_order=request.query_params.get("price_order")
        if(qparam_price_order is not None):
            if(qparam_price_order!="오름차순" & qparam_price_order!="내림차순"):
                raise exceptions.ParseError("product_price_order should be 오름차순 or 내림차순")
            if(qparam_price_order=="오름차순"):
                qs=qs.order_by('price')
            if(qparam_price_order == "내림차순"):
                qs=qs.order_by(-'price')
        qparam_product_name_order=request.query_params.get("product_name_order")
        if(qparam_product_name_order is not None):
            if(qparam_product_name_order!="오름차순" & qparam_product_name_order!="내림차순"):
                raise exceptions.ParseError("product_name_order should be 오름차순 or 내림차순")
            if(qparam_product_name_order == "오름차순"):
                qs=qs.order_by('price')
            if(qparam_product_name_order == "내림차순"):
                qs=qs.order_by(-'price')
        qparam_calory_order=request.query_params.get("calory_order")
        if(qparam_calory_order is not None):
            if(qparam_calory_order!="오름차순" & qparam_calory_order!="내림차순"):
                raise exceptions.ParseError("calory_order should be 오름차순 or 내림차순")
            if(qparam_calory_order == "오름차순"):
                qs=qs.order_by('calory')
            if(qparam_calory_order == "내림차순"):
                qs=qs.order_by(-'calory')
        qparam_product_name=request.query_params.get("product_name")
        if(qparam_product_name is not None):
            qs=qs.filter(product_name__icontains=qparam_product_name)
        qparam_calory_low_range=request.query_params.get("calory_low")
        if(qparam_calory_low_range is not None):
            if(not qparam_calory_low_range.isdigit()):
                raise exceptions.ParseError("칼로리는 숫자만")
            qparam_calory_low_range=int(qparam_calory_low_range)
            qs=qs.filter(calory__gte=qparam_calory_low_range)
        qparam_calory_high_range=request.query_params.get("calory_high")
        if(qparam_calory_high_range is not None):
            if(not qparam_calory_high_range.isdigit()):
                raise exceptions.ParseError("칼로리는 숫자만")
            qparam_calory_high_range=int(qparam_calory_high_range)
            qs=qs.filter(calory__lte=qparam_calory_high_range)
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
    authentication_classes = [JWTCookieAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        price=self.request.query_params.get('price',None)
        rqs=self.queryset.order_by('?')
        if(price==None):
            raise exceptions.ParseError("파라미터가 필요합니다 (가격)")
        if not price.isdigit():
            raise exceptions.ParseError("가격은 숫자만")
        price=int(price)
        if(price<1000):
            raise exceptions.ParseError("가격은 1000원이상")
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
        product_list=self.request.data
        rqs=[]
        for x in product_list:
            meal_list= Daily_Meal.objects.filter(created_at__date=timezone.now().date())
            if(not self.queryset.filter(id=x['id']).exists()):
                raise exceptions.ParseError("존재하지않는 품목입니다")
            if(x['wtime']!="아침" and x['wtime']!="점심" and x['wtime']!="저녁"):
                raise exceptions.ParseError("아침 점심 저녁을 선택해주세요")
            meal_id=1
            if(x['wtime']=="아침"):
                if(not meal_list.filter(morning=True).exists()):
                    meal_id=Daily_Meal.objects.create(user=self.request.user,morning=True)
                else:
                    meal_id=meal_list.filter(morning=True)[0]
            if(x['wtime']=="점심"):
                if(not meal_list.filter(lunch=True).exists()):
                    meal_id=Daily_Meal.objects.create(user=self.request.user,lunch=True)
                else:
                    meal_id=meal_list.filter(lunch=True)[0]
            if(x['wtime']=="저녁"):
                if(not meal_list.filter(dinner=True).exists()):
                    meal_id=Daily_Meal.objects.create(user=self.request.user,dinner=True)
                else:
                    meal_id=meal_list.filter(dinner=True)[0]
            nowp=self.queryset.get(id=x['id'])
            MEAL_PRODUCT.objects.create(meal_id=meal_id,product_id=nowp)
            rqs.append(nowp)
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
            raise exceptions.ParseError("칼로리는 숫자만")
        wtime=self.request.query_params.get('time',None)
        print(wtime)
        if(wtime is None):
            raise exceptions.ParseError("식사할 시간을 입력해주세요 예) 아침 점심 저녁")
        if(wtime!="아침" and wtime!="점심" and wtime!="저녁"):
            raise exceptions.ParseError("식사할 시간을 정확히 입력해주세요 예) 아침 점심 저녁")
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
