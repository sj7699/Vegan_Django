from django.forms import ValidationError
from django.shortcuts import render
from django.contrib.auth.models import User
from userinfo.models import Favor_Category,Product
from .serializers import *
from rest_framework import viewsets,generics
from rest_framework.decorators import action
from rest_framework.response import Response
import random
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
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
        calory=self.request.query_params.get('calory','')
        rqs=self.queryset.order_by('?')
        if not calory.isdigit():
            raise ValidationError("칼로리는 숫자만")
        calory=float(calory)
        c=0
        cutcqs=[]
        for x in rqs:
            nowc=x.calory
            if(nowc+c>calory):
                break
            c+=nowc
            cutcqs.append(x)
        return cutcqs



# Create your views here.
