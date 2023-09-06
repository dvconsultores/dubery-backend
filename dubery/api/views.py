from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializers import *
import django_filters.rest_framework
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
# Create your views here.

class lentesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = lentes.objects.all().order_by('id')
    serializer_class = lentesSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['nombre']
    http_method_names = ['get']
