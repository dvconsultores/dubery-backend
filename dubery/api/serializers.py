from rest_framework import serializers
from .models import *


class lentesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
            model = lentes
            fields = '__all__'
            http_method_names = ['get']
