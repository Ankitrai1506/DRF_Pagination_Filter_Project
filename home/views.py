from django.shortcuts import render
from .serializer import StudentSerializer
from .mypagination import Mypagination
from .models import Student
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
#create

class StudentApiview(ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class= Mypagination
    #filter_backends= [DjangoFilterBackend]
    #filterset_fields= ['city']
    
    #filter_backends = [SearchFilter]     #it use for Search filtering
    #search_fields = ['name']

    filter_backends = [OrderingFilter]
    ordering_fields = ['name']




class StudentDetailedApi(RetrieveUpdateDestroyAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field= 'id'
