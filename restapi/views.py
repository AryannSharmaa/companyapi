from django.shortcuts import render
from rest_framework import viewsets
from restapi.models import Company,Employee
from restapi.serializers import CompanySerializer,EmployeeSerializer
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 