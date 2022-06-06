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

class CutcaloryView(viewsets.ModelViewSet):
    randombag=Product.objects.all().order_by('?')[:10]
    serializer_class=Productserializers


# Create your views here.
