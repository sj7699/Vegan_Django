from rest_framework import serializers
from . models import *

class Favorcategoryserializers(serializers.ModelSerializer):
    class Meta:
        model=Favor_Category
        fields='__all__'
    
