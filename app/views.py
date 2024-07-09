from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from app.serializers import *
from app.models import *
class ProductCrudModelViewSet(ModelViewSet):
    serializer_class=Productserial
    queryset=Product.objects.all()

