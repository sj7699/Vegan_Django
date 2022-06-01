from django.shortcuts import render

from userinfo.models import Favor_Category
from .serializers import Favorcategoryserializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
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
# Create your views here.
